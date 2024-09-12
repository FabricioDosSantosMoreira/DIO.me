using System.Net;
using System.Text;
using System.Text.Json;

using MinimalAPI.API.Dominio.DTOs;
using MinimalAPI.API.Dominio.Entidades;
using MinimalAPI.API.Dominio.ModelViews;
using MinimalAPI.API.Tests.Helpers;

namespace MinimalAPI.API.Test.Requests;

[TestClass]
public class AdministradorRequestTest
{
    [ClassInitialize]
    public static void ClassInit(TestContext testContext)
    {
        Setup.ClassInit(testContext);
    }

    [ClassCleanup]
    public static void ClassCleanup()
    {
        Setup.ClassCleanup();
    }
    
    [TestMethod]
    public async Task TestarLoginAdministrador()
    {
        // Arrange
        var loginDTO = new LoginDTO{
            Email = "adm@teste.com",
            Senha = "123456"
        };

        var content = new StringContent(JsonSerializer.Serialize(loginDTO), Encoding.UTF8,  "Application/json");

        // Act
        var response = await Setup.client.PostAsync("/administradores/login", content);

        // Assert
        Assert.AreEqual(HttpStatusCode.OK, response.StatusCode);

        var result = await response.Content.ReadAsStringAsync();
        var admLogado = JsonSerializer.Deserialize<AdministradorLogado>(result, new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true
        }) ?? throw new Exception();
        
        Assert.IsNotNull(admLogado.Email);
        Assert.IsNotNull(admLogado.Perfil);
        Assert.IsNotNull(admLogado.Token);

        Assert.AreEqual("adm@teste.com", admLogado.Email);
        Assert.AreEqual("Adm", admLogado.Perfil);
    }


    [TestMethod]
    public async Task TestarLoginEditor()
    {
        // Arrange
        var loginDTO = new LoginDTO{
            Email = "editor@teste.com",
            Senha = "123456"
        };

        var content = new StringContent(JsonSerializer.Serialize(loginDTO), Encoding.UTF8,  "Application/json");

        // Act
        var response = await Setup.client.PostAsync("/administradores/login", content);

        // Assert
        Assert.AreEqual(HttpStatusCode.OK, response.StatusCode);

        var result = await response.Content.ReadAsStringAsync();
        var editorLogado = JsonSerializer.Deserialize<AdministradorLogado>(result, new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true
        }) ?? throw new Exception();
        
        Assert.IsNotNull(editorLogado.Email);
        Assert.IsNotNull(editorLogado.Perfil);
        Assert.IsNotNull(editorLogado.Token);

        Assert.AreEqual("editor@teste.com", editorLogado.Email);
        Assert.AreEqual("Editor", editorLogado.Perfil);
    }
}