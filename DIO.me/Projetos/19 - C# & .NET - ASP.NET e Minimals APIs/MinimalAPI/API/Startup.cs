using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;
using Microsoft.OpenApi.Models;

using MinimalAPI.API.Dominio.DTOs;
using MinimalAPI.API.Dominio.Entidades;
using MinimalAPI.API.Dominio.Enums;
using MinimalAPI.API.Dominio.Interfaces;
using MinimalAPI.API.Dominio.ModelViews;
using MinimalAPI.API.Dominio.Servicos;
using MinimalAPI.API.Infraestrutura.DB;

namespace MinimalAPI.API
{
    public class Startup
    {
        private readonly string Key;
        public IConfiguration Configuration { get; set; } = default!;

        public Startup(IConfiguration configuration)

        {
            if(configuration != null)
            {
                Configuration = configuration;
                Key = Configuration.GetSection("Jwt").ToString() ?? string.Empty;
            }
        }


        public void ConfigureServices(IServiceCollection services)
        {  
            services.AddAuthentication(option => {
                option.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
                option.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
                }).AddJwtBearer(option => {
                    option.TokenValidationParameters = new TokenValidationParameters
                    {
                        ValidateLifetime = true,
                        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(Key)),
                        ValidateIssuer = false,
                        ValidateAudience = false
                    };
                });

            services.AddAuthorization();

            services.AddScoped<IAdministradorServico, AdministradorServico>();
            services.AddScoped<IVeiculoServico, VeiculoServico>();

            services.AddEndpointsApiExplorer();
            services.AddSwaggerGen(options => {
                options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
                {
                    Name = "Authorization",
                    Type = SecuritySchemeType.Http,
                    Scheme = "bearer",
                    BearerFormat = "JWT",
                    In = ParameterLocation.Header,
                    Description = "Insira o Token JWT Aqui!"
                });

                options.AddSecurityRequirement(new OpenApiSecurityRequirement
                {
                    {
                        new OpenApiSecurityScheme{
                            Reference = new OpenApiReference 
                            {
                                Type = ReferenceType.SecurityScheme,
                                Id = "Bearer"
                            }
                        },
                        new string[] {}
                    }
                });
            });

            services.AddDbContext<DbContexto>(options => {
                options.UseMySql(
                    Configuration.GetConnectionString("MySql"),
                    ServerVersion.AutoDetect(Configuration.GetConnectionString("MySql"))
                );
            });
        }


        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            app.UseSwagger();
            app.UseSwaggerUI();

            app.UseRouting();

            app.UseAuthentication();
            app.UseAuthorization();

            app.UseEndpoints(endpoints => { 
                #region Home
                endpoints.MapGet("/", () => Results.Json(new Home())).AllowAnonymous().WithTags("Home");
                # endregion 

                #region Administradores
                string GerarTokenJwt(Administrador administrador)
                {
                    if(string.IsNullOrEmpty(Key)) 
                    {
                        return string.Empty;
                    }

                    var securityKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(Key));
                    var credentials = new SigningCredentials(securityKey, SecurityAlgorithms.HmacSha256);

                    var claims = new List<Claim>()
                    {
                        new Claim("Email", administrador.Email),
                        new Claim("Perfil", administrador.Perfil),
                        new Claim(ClaimTypes.Role, administrador.Perfil),
                    };

                    var token = new JwtSecurityToken(
                        claims: claims,
                        expires: DateTime.Now.AddDays(1),
                        signingCredentials: credentials
                    );

                    return new JwtSecurityTokenHandler().WriteToken(token);
                }


                endpoints.MapPost("/administradores/login", ([FromBody] LoginDTO loginDTO, IAdministradorServico administradorServico) => {
                    
                    var adm = administradorServico.Login(loginDTO);
                    if(adm != null)
                    {
                        string token = GerarTokenJwt(adm);

                        return Results.Ok(new AdministradorLogado{
                            Email = adm.Email,
                            Perfil = adm.Perfil,
                            Token = token
                        });
                    }
                    else
                    {
                        return Results.Unauthorized();
                    }
                })
                .AllowAnonymous()
                .WithTags("Administradores");


                endpoints.MapGet("/administradores", ([FromQuery] int? pagina, IAdministradorServico administradorServico) => {

                    var adms = new List<AdministradorModelView>();
                    List<Administrador> administradores = administradorServico.Todos(pagina);

                    foreach (var adm in administradores)
                    {
                        adms.Add(new AdministradorModelView{
                            Id = adm.Id,
                            Email = adm.Email,
                            Perfil = adm.Perfil
                        });
                    }

                    return Results.Ok(adms);
                })
                .RequireAuthorization()
                .RequireAuthorization(new AuthorizeAttribute { Roles = "Adm" })
                .WithTags("Administradores");


                endpoints.MapGet("/administradores/{id}", ([FromRoute] int id, IAdministradorServico administradorServico) => {

                    Administrador administrador = administradorServico.BuscaPorId(id);
                    if(administrador == null)
                    {
                        return Results.NotFound();
                    }

                    var adm = new AdministradorModelView{
                        Id = administrador.Id,
                        Email = administrador.Email,
                        Perfil = administrador.Perfil
                    };

                    return Results.Ok(adm);
                })
                .RequireAuthorization()
                .RequireAuthorization(new AuthorizeAttribute { Roles = "Adm"})
                .WithTags("Administradores");


                endpoints.MapPost("/administradores", ([FromBody] AdministradorDTO administradorDTO, IAdministradorServico administradorServico) => {

                    var validacao = new ErrosDeValidacao{
                        Mensagens = new List<string>()
                    };

                    if(string.IsNullOrEmpty(administradorDTO.Email))
                    {
                        validacao.Mensagens.Add("O E-mail não pode ser vazio");
                    }

                    if(string.IsNullOrEmpty(administradorDTO.Senha))
                    {
                        validacao.Mensagens.Add("A Senha não pode ser vazia");
                    }

                    if(administradorDTO.Perfil == null)
                    {
                        validacao.Mensagens.Add("O Perfil não pode ser vazio");
                    }

                    if(validacao.Mensagens.Count > 0) 
                    {
                        return Results.BadRequest(validacao);
                    }
                    
                    Administrador administrador = new Administrador {
                        Email = administradorDTO.Email,
                        Senha = administradorDTO.Senha,
                        // OBS: Se vier nulo recebe 'Editor'
                        Perfil = administradorDTO.Perfil.ToString() ?? Perfil.Editor.ToString() 
                    };

                    administradorServico.Incluir(administrador);

                    var adm = new AdministradorModelView{
                        Id = administrador.Id,
                        Email = administrador.Email,
                        Perfil = administrador.Perfil
                    };

                    return Results.Created($"/administrador/{administrador.Id}", adm);
                })
                .RequireAuthorization()
                .RequireAuthorization(new AuthorizeAttribute { Roles = "Adm"})
                .WithTags("Administradores");
                #endregion

                #region Veiculos
                ErrosDeValidacao ValidaDTO(VeiculoDTO veiculoDTO)
                {
                    var validacao = new ErrosDeValidacao{
                        Mensagens = new List<string>()
                    };

                    if(string.IsNullOrEmpty(veiculoDTO.Nome))
                    {
                        validacao.Mensagens.Add("O nome não pode ser vazio");
                    }
                    if(string.IsNullOrEmpty(veiculoDTO.Marca))
                    {
                        validacao.Mensagens.Add("A Marca não pode ficar em branco");
                    }
                    if(veiculoDTO.Ano < 1900)
                    {
                        validacao.Mensagens.Add("Veículo muito antigo, aceito somente anos superiores à 1900");
                    }

                    return validacao;
                }


                endpoints.MapPost("/veiculos", ([FromBody] VeiculoDTO veiculoDTO, IVeiculoServico veiculoServico) => {
                    
                    var validacao = ValidaDTO(veiculoDTO);
                    if(validacao.Mensagens.Count > 0)
                    {
                        return Results.BadRequest(validacao);
                    }

                    Veiculo veiculo = new Veiculo {
                        Nome = veiculoDTO.Nome,
                        Marca = veiculoDTO.Marca,
                        Ano = veiculoDTO.Ano
                    };

                    veiculoServico.Incluir(veiculo);

                    return Results.Created($"/veiculo/{veiculo.Id}", veiculo);
                })
                .RequireAuthorization()
                .RequireAuthorization(new AuthorizeAttribute { Roles = "Adm,Editor"})
                .WithTags("Veículos");


                endpoints.MapGet("/veiculos", ([FromQuery] int? pagina, IVeiculoServico veiculoServico) => {

                    List<Veiculo> veiculos = veiculoServico.Todos(pagina);

                    return Results.Ok(veiculos);

                })
                .RequireAuthorization()
                .WithTags("Veículos");


                endpoints.MapGet("/veiculos/{id}", ([FromRoute] int id, IVeiculoServico veiculoServico) => {

                    Veiculo veiculo = veiculoServico.BuscaPorId(id);
                    if(veiculo == null)
                    {
                        return Results.NotFound();
                    }

                    return Results.Ok(veiculo);
                })
                .RequireAuthorization()
                .RequireAuthorization(new AuthorizeAttribute { Roles = "Adm,Editor"})
                .WithTags("Veículos");


                endpoints.MapPut("/veiculos/{id}", ([FromRoute] int id, VeiculoDTO veiculoDTO, IVeiculoServico veiculoServico) => {

                    Veiculo veiculo = veiculoServico.BuscaPorId(id);
                    if(veiculo == null)
                    {
                        return Results.NotFound();
                    }

                    var validacao = ValidaDTO(veiculoDTO);
                    if(validacao.Mensagens.Count > 0) 
                    {
                        return Results.BadRequest(validacao);
                    }
                        
                    veiculo.Nome = veiculoDTO.Nome;
                    veiculo.Marca = veiculoDTO.Marca;
                    veiculo.Ano = veiculoDTO.Ano;

                    veiculoServico.Atualizar(veiculo);

                    return Results.Ok(veiculo);
                })
                .RequireAuthorization()
                .RequireAuthorization(new AuthorizeAttribute { Roles = "Adm"})
                .WithTags("Veículos");


                endpoints.MapDelete("/veiculos/{id}", ([FromRoute] int id, IVeiculoServico veiculoServico) => {

                    Veiculo veiculo = veiculoServico.BuscaPorId(id);
                    if(veiculo == null)
                    {
                        return Results.NotFound();
                    }

                    veiculoServico.Apagar(veiculo);

                    return Results.NoContent();

                })
                .RequireAuthorization()
                .RequireAuthorization(new AuthorizeAttribute { Roles = "Adm"})
                .WithTags("Veículos");
                #endregion
            });
        }
    }
}