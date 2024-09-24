using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Propriedades.Models
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
            foreach (Pessoa aluno in Alunos)
            {
                Console.WriteLine($"{aluno.NomeCompleto}");            
            }
        }
    }
}