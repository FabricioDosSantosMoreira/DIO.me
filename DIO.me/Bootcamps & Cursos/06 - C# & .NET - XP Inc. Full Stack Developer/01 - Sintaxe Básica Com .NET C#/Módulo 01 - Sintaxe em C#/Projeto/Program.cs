using Sintaxe.Classes;//Projeto.Models;

class Program
    {
        static void Main(string[] args)
        {

        // Instanciando um objeto da classe Pessoa
        Pessoa pessoa = new()
        {
            // Definindo valores para as propriedades nome e idade
            Nome = "Fabrício",
            Idade = 19
        };
        
        // Chamando o método Apresentar
        pessoa.Apresentar();
        }
    }
