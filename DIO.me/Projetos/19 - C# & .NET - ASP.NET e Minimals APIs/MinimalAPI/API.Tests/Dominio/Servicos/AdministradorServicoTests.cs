using Microsoft.EntityFrameworkCore;

using MinimalAPI.API.Dominio.Entidades;
using MinimalAPI.API.Dominio.Servicos;

namespace MinimalAPI.API.Tests.Dominio.Servicos
{   
    [TestClass]
    public class AdministradorServicoTest
    {
        [TestMethod]
        public void TestandoSalvarAdministrador()
        {
            var context = CriarContexto.CriarContextoDeTeste();
            context.Database.ExecuteSqlRaw("TRUNCATE TABLE Administradores");

            var administradorServico = new AdministradorServico(context);

            var adm = new Administrador
            {
                Email = "Administrador@teste.com",
                Senha = "1234567890",
                Perfil = "Adm"
            };

            administradorServico.Incluir(adm);

            Assert.AreEqual(1, administradorServico.Todos(1).Count);
        }


        [TestMethod]
        public void TestandoBuscarTodosAdministradores()
        {
            var context = CriarContexto.CriarContextoDeTeste();
            context.Database.ExecuteSqlRaw("TRUNCATE TABLE Administradores");

            var administradorServico = new AdministradorServico(context);

            var adm1 = new Administrador
            {
                Email = "Administrador1@teste.com",
                Senha = "1234567890",
                Perfil = "Adm"
            };
            var adm2 = new Administrador
            {
                Email = "Administrador2@teste.com",
                Senha = "1234567890",
                Perfil = "Adm"
            };

            administradorServico.Incluir(adm1);
            administradorServico.Incluir(adm2);

            Assert.AreEqual(2, administradorServico.Todos(1).Count);
        }


        [TestMethod]
        public void TestandoBuscarAdministradorPorId()
        {
            var context = CriarContexto.CriarContextoDeTeste();
            context.Database.ExecuteSqlRaw("TRUNCATE TABLE Administradores");

            var administradorServico = new AdministradorServico(context);

            var adm = new Administrador
            {
                Email = "Administrador@teste.com",
                Senha = "1234567890",
                Perfil = "Adm"
            };

            administradorServico.Incluir(adm);

            Administrador administradorDoBanco = administradorServico.BuscaPorId(1) ?? throw new Exception();

            Assert.AreEqual(1, administradorDoBanco.Id);
            Assert.AreEqual("Administrador@teste.com", administradorDoBanco.Email);
            Assert.AreEqual("1234567890", administradorDoBanco.Senha);
            Assert.AreEqual("Adm", administradorDoBanco.Perfil);
        }
    }
}