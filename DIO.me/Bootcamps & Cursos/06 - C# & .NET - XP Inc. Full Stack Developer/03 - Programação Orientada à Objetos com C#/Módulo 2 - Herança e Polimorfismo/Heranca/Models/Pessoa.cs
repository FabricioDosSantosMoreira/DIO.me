using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Heranca.Models
{
    public class Pessoa
    {
        // Propriedades
        public string Nome { get; set; }
        public int Idade { get; set; }

        public void Apresentar() 
        {
            Console.WriteLine($"Olá, meu nome é {Nome} e tenho {Idade} anos");
        }
    }
}