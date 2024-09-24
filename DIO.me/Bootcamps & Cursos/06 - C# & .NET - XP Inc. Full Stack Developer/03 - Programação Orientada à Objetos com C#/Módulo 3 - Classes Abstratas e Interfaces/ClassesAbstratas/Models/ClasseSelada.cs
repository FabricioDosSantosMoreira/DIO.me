using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ClassesAbstratas.Models
{
    // Uma classe selada impede que outras classes façam uma herança dela, ou seja, nenhuma classe pode ser sua derivada
    public sealed class ClasseSelada : Pessoa
    {
        public ClasseSelada(string nome) : base(nome) { }

        // Método Selado
        public sealed override void Apresentar()
        {
            base.Apresentar();
            Console.WriteLine("Método selado!");
        }
    }
}