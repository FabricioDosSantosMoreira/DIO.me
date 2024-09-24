using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Calculadora.Services;

namespace CalculadoraTestes
{
    public class ValidadorStringTests
    {

        private readonly ValidadorString _validador;

        public ValidadorStringTests() 
        {
            _validador = new ValidadorString();
        }

        [Fact]
        public void DeveContarQuatroCaracteresEmGatoERetornarQuatro()
        {
            string texto = "Gato";

            int resultado = _validador.ContaCaracteres(texto);

            Assert.Equal(4, resultado);
        }
    }
}