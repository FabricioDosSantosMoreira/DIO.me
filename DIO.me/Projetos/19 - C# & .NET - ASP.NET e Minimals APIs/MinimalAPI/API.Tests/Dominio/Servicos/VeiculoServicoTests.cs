using Microsoft.EntityFrameworkCore;

using MinimalAPI.API.Dominio.Entidades;
using MinimalAPI.API.Dominio.Servicos;

namespace MinimalAPI.API.Tests.Dominio.Servicos
{   
    [TestClass]
    public class VeiculoServicoTests
    {
        [TestMethod]
        public void TestandoSalvarVeiculo()
        {
            var context = CriarContexto.CriarContextoDeTeste();
            context.Database.ExecuteSqlRaw("TRUNCATE TABLE Veiculos");

            var veiculoServico = new VeiculoServico(context);

            var veiculo = new Veiculo
            {
                Nome = "TesteNome",
                Marca = "TesteMarca",
                Ano = 2000
            };

            veiculoServico.Incluir(veiculo);

            Assert.AreEqual(1, veiculoServico.Todos(1).Count);
        }


        [TestMethod]
        public void TestandoBuscarTodosVeiculos()
        {
            var context = CriarContexto.CriarContextoDeTeste();
            context.Database.ExecuteSqlRaw("TRUNCATE TABLE Veiculos");

            var veiculoServico = new VeiculoServico(context);

            var veiculo1 = new Veiculo
            {
                Nome = "Veículo1",
                Marca = "Marca1",
                Ano = 2000
            };
            var veiculo2 = new Veiculo
            {
                Nome = "Veículo2",
                Marca = "Marca2",
                Ano = 2020
            };

            veiculoServico.Incluir(veiculo1);
            veiculoServico.Incluir(veiculo2);

            Assert.AreEqual(2, veiculoServico.Todos(1).Count);
        }


        [TestMethod]
        public void TestandoBuscarVeiculoPorId()
        {
            var context = CriarContexto.CriarContextoDeTeste();
            context.Database.ExecuteSqlRaw("TRUNCATE TABLE Veiculos");

            var veiculoServico = new VeiculoServico(context);

            var veiculo = new Veiculo
            {
                Nome = "Veículo",
                Marca = "Marca",
                Ano = 2000
            };

            veiculoServico.Incluir(veiculo);

            Veiculo veiculoDoBanco = veiculoServico.BuscaPorId(1) ?? throw new Exception();

            Assert.AreEqual(1, veiculoDoBanco.Id);
            Assert.AreEqual("Veículo", veiculoDoBanco.Nome);
            Assert.AreEqual("Marca", veiculoDoBanco.Marca);
            Assert.AreEqual(2000, veiculoDoBanco.Ano);
        }
    }
}