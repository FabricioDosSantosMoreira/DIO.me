using MinimalAPI.API.Dominio.Entidades;

namespace MinimalAPI.Tests.Domain.Entidades
{
    [TestClass]
    public class AdministradorTest
    {
        [TestMethod]
        public void TestarGetSetAdministrador()
        {
            var adm = new Administrador();

            adm.Id = 1;
            adm.Email = "Teste@teste.com";
            adm.Senha = "12345678";
            adm.Perfil = "Adm";

            Assert.AreEqual(1, adm.Id);
            Assert.AreEqual("Teste@teste.com", adm.Email);
            Assert.AreEqual("12345678", adm.Senha);
            Assert.AreEqual("Adm", adm.Perfil);
        }
    }
}