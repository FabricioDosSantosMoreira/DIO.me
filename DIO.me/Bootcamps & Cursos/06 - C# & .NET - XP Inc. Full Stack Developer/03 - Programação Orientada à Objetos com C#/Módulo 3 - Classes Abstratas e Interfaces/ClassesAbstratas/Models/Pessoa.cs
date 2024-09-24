using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ClassesAbstratas.Models
{
    public class Pessoa
    {
        public Pessoa(string nome)
        {
            Nome = nome;
        }

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