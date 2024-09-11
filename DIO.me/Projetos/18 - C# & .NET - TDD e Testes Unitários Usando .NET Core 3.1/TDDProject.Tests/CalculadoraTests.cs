using System;
using Xunit;
using Xunit.Abstractions;

using TDDProject.Services;
using System.Linq;

namespace TDDProject.Tests
{
    public class CalculadoraTests
    {
        // dotnet test --logger "console;verbosity=detailed"
        private readonly ITestOutputHelper _output;

        public CalculadoraTests(ITestOutputHelper output)
        {
            _output = output;
        }

        public CalculadoraImpl ConstruirClasse()
        {
            string Data = DateTime.Now.ToString("dd/MM/yyyy - HH:mm");
            CalculadoraImpl _calculadora = new CalculadoraImpl(Data);

            return _calculadora;
        }

        [Fact]
        public void SomarFactTest()
        {
            CalculadoraImpl _calculadora = ConstruirClasse();

            int resultado = _calculadora.Somar(5, 7);

            Assert.Equal(12, resultado);
        }

        [Theory]
        [InlineData (8, 2, 10)]
        [InlineData (5, 5, 10)]
        [InlineData (2, 3, 5)]
        [InlineData (1, 2, 3)]
        public void SomarTest(int num1, int num2, int resultado)
        {
            CalculadoraImpl _calculadora = ConstruirClasse();

            int resultadoDaCalculadora = _calculadora.Somar(num1, num2);

            Assert.Equal(resultado, resultadoDaCalculadora);
        }

        [Theory]
        [InlineData (8, 2, 6)]
        [InlineData (5, 5, 0)]
        [InlineData (6, 3, 3)]
        [InlineData (2, 1, 1)]
        public void SubtrairTest(int num1, int num2, int resultado)
        {
            CalculadoraImpl _calculadora = ConstruirClasse();

            int resultadoDaCalculadora = _calculadora.Subtrair(num1, num2);

            Assert.Equal(resultado, resultadoDaCalculadora);
        }

        [Theory]
        [InlineData (8, 2, 16)]
        [InlineData (5, 5, 25)]
        [InlineData (2, 3, 6)]
        [InlineData (1, 2, 2)]
        public void MultiplicarTest(int num1, int num2, int resultado)
        {
            CalculadoraImpl _calculadora = ConstruirClasse();

            int resultadoDaCalculadora = _calculadora.Multiplicar(num1, num2);

            Assert.Equal(resultado, resultadoDaCalculadora);
        }

        [Theory]
        [InlineData (8, 2, 4)]
        [InlineData (5, 5, 1)]
        [InlineData (6, 3, 2)]
        [InlineData (2, 1, 2)]
        public void DividirTest(int num1, int num2, int resultado)
        {
            CalculadoraImpl _calculadora = ConstruirClasse();

            int resultadoDaCalculadora = _calculadora.Dividir(num1, num2);

            Assert.Equal(resultado, resultadoDaCalculadora);
        }

        [Fact]
        public void DividirPorZeroTest()
        {
            CalculadoraImpl _calculadora = ConstruirClasse();

            Assert.Throws<DivideByZeroException>(
                () => _calculadora.Dividir(3, 0)
            );
        }

        [Fact]
        public void HistoricoTest()
        {
            CalculadoraImpl _calculadora = ConstruirClasse();

            _calculadora.Somar(10, 1);
            _calculadora.Subtrair(10, 2);
            _calculadora.Somar(10, 3);
            _calculadora.Subtrair(10, 4);

            var historico = _calculadora.Historico();

            _output.WriteLine($"\nResultado do Teste ['HistoricoTest']: \n\t{historico[0]}, \n\t{historico[1]}, \n\t{historico[2]}");

            Assert.NotEmpty(historico);
            Assert.Equal(3, historico.Count);
        }
    }
}