using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace TDDProject.Services
{
    public class CalculadoraImpl
    {   
        private readonly List<string> _historico;
        private string Data;

        public CalculadoraImpl(string data)
        {
            _historico = new List<string>();
            Data = data;
        }

        public int Somar(int num1, int num2)
        {
            int res = num1 + num2;
            _historico.Insert(0, $"[{Data}] [Somar] - [num1={num1}, num2={num2}, res={res}]");

            return res;
        }

        public int Subtrair(int num1, int num2)
        {
            int res = num1 - num2;
            _historico.Insert(0, $"[{Data}] [Subtrair] - [num1={num1}, num2={num2}, res={res}]");

            return res;
        }

        public int Multiplicar(int num1, int num2)
        {
            int res = num1 * num2;
            _historico.Insert(0, $"[{Data}] [Multiplicar] - [num1={num1}, num2={num2}, res={res}]");

            return res;
        }

        public int Dividir(int num1, int num2)
        {
            int res = num1 / num2;
            _historico.Insert(0, $"[{Data}] [Dividir] - [num1={num1}, num2={num2}, res={res}]");

            return res;
        }

        public List<string> Historico()
        {
            // Remove do index '3' até 'Count - 3', deixando somente os 3 primeiros itens
            _historico.RemoveRange(3, _historico.Count - 3);

            return _historico;
        }
    }
}