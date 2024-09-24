using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ExemploTuplas.Models
{
    public class Pessoa
    {
        // Métodos Construtores
        public Pessoa() {}

        public Pessoa(string nome, string sobrenome, int idade)
        {
            Nome = nome;
            Sobrenome = sobrenome;
            Idade = idade;
        }

        // Método Desconstrutor
        public void Deconstruct(out string nome, out string sobrenome)
        {
            nome = Nome;
            sobrenome = Sobrenome;
        }



        // Campos
        private string _nome;
        private int _idade;   

        // Propriedades
        public string Nome 
        { 
            // Body Expressions (=>)
            get => _nome; // Ou usar as chaves com a apalavra chave return. Ex: { return _nome.ToUpper()}
            
            // set => _nome = value;
            set
            {
                if (value == "")
                {
                    throw new ArgumentException("O Nome não pode ser vazio");
                }
                _nome = value;
            } 
        }

        public string Sobrenome { get; set; }        
        public string NomeCompleto => $"{Nome} {Sobrenome}".ToUpper();

        public int Idade { 
            get
            {
                return _idade;
            }
            
            set
            {
                if (value < 0)
                {
                    throw new ArgumentException("A Idade não pode ser menor que 0");
                }
                _idade = value;
            }    
        }

        public void Apresentar() 
        {
            Console.WriteLine($"Nome: {NomeCompleto}, Idade: {Idade}");
        }
    }
}
