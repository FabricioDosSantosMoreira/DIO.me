using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ManipulandoValores.Models
{
    public class Curso
    {
        public string Nome { get; set; }
        public List<Pessoa> Alunos { get; set; }
        
        public void AdicionarAluno(Pessoa aluno)
        {
            Alunos.Add(aluno);
        }

        public bool RemoverAluno(Pessoa aluno)
        {
            bool foiRemovido = Alunos.Remove(aluno);
            return foiRemovido;        
        }

        public int ObterQuantidadeDeAlunosMatriculados()
        {
            int quantidade = Alunos.Count;
            return quantidade;
        }

        public void ListarAlunos()
        {   
            Console.WriteLine($"\nAlunos do curso de {Nome}:");

            for (int i = 0; i < Alunos.Count; i++)
            {   
                // Concatenação de strings
                string texto = "Aluno N°" + i + " " + Alunos[i].NomeCompleto;

                // Interpolação de strings
                texto = $"Aluno N°{i + 1}: ['{Alunos[i].NomeCompleto}']";

                Console.WriteLine($"Aluno N°{i + 1}: ['{Alunos[i].NomeCompleto}']"); 
            }
        }
    }
}
