using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ClassesAbstratas.Models
{
    public class ContaCorrente : Conta
    {
        // Necessário implementar os métodos abstratos de 'Conta'
        public override void Creditar(decimal valor)
        {
            if (valor > 0)
            {
                saldo += valor;
                Console.WriteLine($"\nCreditado {valor:C} em seu saldo!");                
            }
            else
            {
                Console.WriteLine($"\nO valor {valor:C} é inválido!");
            }
        }
    }
}