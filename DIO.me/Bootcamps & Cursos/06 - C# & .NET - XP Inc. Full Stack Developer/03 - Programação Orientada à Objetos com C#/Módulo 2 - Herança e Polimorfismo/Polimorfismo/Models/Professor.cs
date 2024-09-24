using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Polimorfismo.Models
{
    public class Professor : Pessoa
    {
        public decimal Salario { get; set; }   

        public override void Apresentar()
        {
            Console.WriteLine($"Olá, meu nome é {Nome}, tenho {Idade} anos e meu salário é {Salario:C}");
        }

        public void Apresentar(bool esconderSalario)
        {
            if (esconderSalario) 
            {
                Console.WriteLine($"Olá, meu nome é {Nome}, tenho {Idade} anos e sou professor!");
            }
            else
            {
                Apresentar();
            }
            
        }
    }
}