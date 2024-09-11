using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjetoValidador.Services
{
    public class ValidadorString
    {
        public int ObterQuantidadeCaracteresDoTexto(string texto)
        {
            return texto.Length;
        }

        public bool TextoContemPalavra(string texto, string palavra)
        {
            return texto.Contains(palavra);
        }

        public bool TextoTerminaComPalavra(string texto, string palavra)
        {
            return texto.EndsWith(palavra);
        }
    }
}