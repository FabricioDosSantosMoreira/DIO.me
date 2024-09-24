using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Encapsulamento.Models
{
    public class ContaCorrente
    {
        public ContaCorrente(int numero) 
        {
            Numero = numero;
        }

        public int Numero { get; set; }
        private decimal Saldo;

        public void Sacar(decimal valor)
        {   
            if (Saldo >= valor) 
            {
                if (valor <= 0) 
                {
                    Console.WriteLine($"\nO valor {valor:C} é inválido!");
                }
                else 
                {
                    Saldo -= valor;
                    Console.WriteLine($"\nFoi sacado {valor:C} de sua conta!");
                }
            }
            else 
            {
                Console.WriteLine("\nSaldo insuficiente para saque!");
            }
        }

        public void Depositar(decimal valor)
        {
            if (valor > 0) 
            {
                Saldo += valor;
                Console.WriteLine($"\nFoi depositado {valor:C} em sua conta!");
            }
            else 
            {
                Console.WriteLine($"\nO valor {valor:C} é inválido!");
            }
        }

        public void ExibirSaldo()
        {
            Console.WriteLine($"\nSaldo disponível: {Saldo:C}");
        }
    }
}