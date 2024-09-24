using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ClassesAbstratas.Models
{
    public class Aluno : Pessoa
    {
        // Construtor por Herança
        public Aluno(string nome) : base(nome) { }

        public double Nota { get; set; }

        public override void Apresentar()
        {
            Console.WriteLine($"Olá, meu nome é {Nome}, tenho {Idade} anos e sou um aluno nota {Nota:F}");
        }
        
    }
}