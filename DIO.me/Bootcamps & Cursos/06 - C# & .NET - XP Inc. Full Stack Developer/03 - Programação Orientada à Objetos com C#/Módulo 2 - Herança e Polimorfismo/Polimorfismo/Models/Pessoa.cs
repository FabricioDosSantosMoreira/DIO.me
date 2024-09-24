using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Polimorfismo.Models
{
    public class Pessoa
    {
        // Propriedades
        public string Nome { get; set; }
        public int Idade { get; set; }

        // 'virtual' significa que pode ser sobreescrito
        public virtual void Apresentar() 
        {
            Console.WriteLine($"Olá, meu nome é {Nome} e tenho {Idade} anos");
        }
    }
}