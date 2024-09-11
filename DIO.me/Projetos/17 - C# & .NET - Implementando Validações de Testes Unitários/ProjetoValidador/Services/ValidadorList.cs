using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjetoValidador.Services
{
    public class ValidadorList
    {
        public List<int> RemoverNumerosNegativos(List<int> lista)
        {
            return lista.Where(x => x > 0).ToList();
        }

        public bool ContemDeterminadoNumero(List<int> lista, int numero)
        {
            return lista.Contains(numero);
        }

        public List<int> MultiplicarItensPorNumero(List<int> lista, int numero)
        {
            return lista.Select(x => x * numero).ToList();
        }

        public int ObterMaiorNumero(List<int> lista)
        {
            return lista.Max();
        }

        public int ObterMenorNumero(List<int> lista)
        {
            return lista.Min();
        }
    }
}