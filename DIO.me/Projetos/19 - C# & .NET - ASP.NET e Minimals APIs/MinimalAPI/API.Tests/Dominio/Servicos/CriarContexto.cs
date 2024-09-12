using System.Reflection;

using Microsoft.Extensions.Configuration;

using MinimalAPI.API.Infraestrutura.DB;

namespace MinimalAPI.API.Tests.Dominio.Servicos
{
    public class CriarContexto
    {
        public static DbContexto CriarContextoDeTeste()
        {
            var assemblyPath = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
            var path = Path.GetFullPath(Path.Combine(assemblyPath ?? "", "..", "..", ".."));

            var builder = new ConfigurationBuilder()
                .SetBasePath(path ?? Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
                .AddEnvironmentVariables();

            var configuration = builder.Build();

            return new DbContexto(configuration);
        }
    }
}