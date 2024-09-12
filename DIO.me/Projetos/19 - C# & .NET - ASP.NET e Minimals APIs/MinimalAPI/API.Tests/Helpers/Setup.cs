using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.Extensions.DependencyInjection;

using MinimalAPI.API.Dominio.Interfaces;
using MinimalAPI.API.Tests.Mocks;

namespace MinimalAPI.API.Tests.Helpers
{
    public class Setup
    {
        public const string PORT = "5001";
        public static TestContext testContext = default!;
        public static WebApplicationFactory<Startup> http = default!;
        public static HttpClient client = default!;

        public static void ClassInit(TestContext testContext)
        {
            Setup.testContext = testContext;
            Setup.http = new WebApplicationFactory<Startup>();

            Setup.http = Setup.http.WithWebHostBuilder(builder =>
            {
                builder.UseSetting("https_port", Setup.PORT).UseEnvironment("Testing");
                
                builder.ConfigureServices(services =>
                {
                    services.AddScoped<IAdministradorServico, AdministradorServicoMock>();
                });

            });

            Setup.client = Setup.http.CreateClient();
        }

        public static void ClassCleanup()
        {
            Setup.http.Dispose();
        }
    }
}