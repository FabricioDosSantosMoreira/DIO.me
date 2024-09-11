using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using ProjetoValidador.Services;

namespace ProjetoValidador.Tests
{
    public class ValidadorListTests
    {
        private readonly ValidadorList _validadorList;

        public ValidadorListTests()
        {
            _validadorList = new ValidadorList();
        }
        
        [Fact]
        public void DeveRemoverNumerosNegativosDeUmaLista()
        {
            List<int> lista = [1, 2, 3, -3, -2, -1, 9, -9, 0];

            List<int> resultado = _validadorList.RemoverNumerosNegativos(lista);

            Assert.All(resultado, num => Assert.True(num >= 0));
        }

        [Fact]
        public void DeveConterONumero9NaLista()
        {
            List<int> lista = [1, 2, 3, -3, -2, -1, 9, -9, 0];
            int numero = 9;

            bool resultado = _validadorList.ContemDeterminadoNumero(lista, numero);

            Assert.True(resultado);
        }

        [Fact]
        public void NaoDeveConterONumero10NaLista()
        {
            List<int> lista = [1, 2, 3, -3, -2, -1, 9, -9, 0];
            int numero = 10;

            bool resultado = _validadorList.ContemDeterminadoNumero(lista, numero);

            Assert.False(resultado);
        }

        [Fact]
        public void DeveMultiplicarOsElementosDaListaPor2()
        {
            List<int> lista = [1, 2, 3, -3, -2, -1, 9, -9, 0];
            int numero = 2;

            List<int> resultado = _validadorList.MultiplicarItensPorNumero(lista, numero);
            List<int> resultadoAlvo = [2, 4, 6, -6, -4, -2, 18, -18, 0];

            Assert.Equal(resultadoAlvo, resultado);

            Assert.All(lista, item =>
            {
                int idx = lista.IndexOf(item);
                Assert.Equal(item * numero, resultado[idx]);
            });
        }

        [Fact]
        public void DeveRetornar9ComoMaiorNumeroDaLista()
        {
            List<int> lista = [1, 2, 3, -3, -2, -1, 9, -9, 0];

            int resultado = _validadorList.ObterMaiorNumero(lista);
            int resultadoAlvo = 9;

            Assert.Equal(resultadoAlvo, resultado);
            Assert.Equal(lista.Max(), resultado);
        }

        [Fact]
        public void DeveRetornarOitoNegativoComoMenorNumeroDaLista()
        {
            List<int> lista = [1, -1, 2, -2, 3, -3, 4, 5, 6, 7, -7, 8, -8, 10];

            int resultado = _validadorList.ObterMenorNumero(lista);
            int resultadoAlvo = -8;

            Assert.Equal(resultadoAlvo, resultado);
            Assert.Equal(lista.Min(), resultado);
        }
    }
}