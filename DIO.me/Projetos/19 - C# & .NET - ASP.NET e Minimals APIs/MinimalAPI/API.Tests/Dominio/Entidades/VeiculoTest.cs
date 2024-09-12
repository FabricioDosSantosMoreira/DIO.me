using MinimalAPI.API.Dominio.Entidades;

namespace MinimalAPI.API.Tests.Dominio.Entidades
{
    [TestClass]
    public class VeiculoTest
    {
        [TestMethod]
        public void TestarGetSetVeiculo()
        {
            var veiculo = new Veiculo();

            veiculo.Id = 1;
            veiculo.Nome = "TesteNome";
            veiculo.Marca = "TesteMarca";
            veiculo.Ano = 2000;

            Assert.AreEqual(1, veiculo.Id);
            Assert.AreEqual("TesteNome", veiculo.Nome);
            Assert.AreEqual("TesteMarca", veiculo.Marca);
            Assert.AreEqual(2000, veiculo.Ano);
        }
    }
}