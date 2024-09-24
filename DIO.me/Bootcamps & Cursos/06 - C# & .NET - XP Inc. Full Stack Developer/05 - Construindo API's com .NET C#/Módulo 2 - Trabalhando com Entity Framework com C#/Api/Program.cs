using Microsoft.EntityFrameworkCore;

using Api.Context;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<AgendaContext>(options => 
    options.UseSqlServer(builder.Configuration.GetConnectionString("ConexaoPadrao")));

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.MapControllers();
app.Run();