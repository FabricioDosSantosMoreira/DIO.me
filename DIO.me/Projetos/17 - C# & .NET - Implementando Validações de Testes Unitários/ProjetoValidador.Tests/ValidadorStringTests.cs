using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using ProjetoValidador.Services;

namespace ProjetoValidador.Tests
{
    public class ValidadorStringTests
    {
        private readonly ValidadorString _validorString;

        public ValidadorStringTests()
        {
            _validorString = new ValidadorString();
        }

        [Fact]
        public void DeveRetornar6QuantidadeCaracteresDaPalavraMatrix()
        {
            string texto = "Matrix";

            int resultado = _validorString.ObterQuantidadeCaracteresDoTexto(texto);

            Assert.Equal(6, resultado);
        }

        [Fact]
        public void DeveConterAPalavraQualquerNoTexto()
        {
            string texto = "Esse é um texto qualquer";
            string palavra = "qualquer";

            bool resultado = _validorString.TextoContemPalavra(texto, palavra);

            Assert.True(resultado);
        }

        [Fact]
        public void NaoDeveConterAPalavraTesteNoTexto()
        {
            string texto = "Esse é um texto qualquer";
            string palavra = "teste";

            bool resultado = _validorString.TextoContemPalavra(texto, palavra);

            Assert.False(resultado);
        }

        [Fact]
        public void TextoDeveTerminarComAPalavraProcurado()
        {
            string texto = "Começo, meio e fim do texto procurado";
            string palavra = "procurado";

            bool resultado = _validorString.TextoTerminaComPalavra(texto, palavra);

            Assert.True(resultado);
        }
    }
}