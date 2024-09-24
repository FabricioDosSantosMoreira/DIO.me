using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ClassesAbstratas.Models
{
    public abstract class Conta
    {
        protected decimal saldo;

        // Método abstrato
        public abstract void Creditar(decimal valor);

        public void ExibirSaldo()
        {
            Console.WriteLine($"\nSaldo Atual: {saldo:C}");
        }
    }
}