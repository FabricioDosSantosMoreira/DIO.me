using Propriedades.Models;

Pessoa p1 = new Pessoa(nome: "Fabrício", sobrenome: "dos Santos Moreira", idade: 19);

Pessoa p2 = new Pessoa();
p2.Nome = "Nome";
p2.Sobrenome = "Sobrenome";
p2.Idade = 19;


Curso cursoDeingles = new Curso{
    Nome = "Inglês",
    Alunos = new List<Pessoa>()
};


cursoDeingles.AdicionarAluno(p1);
cursoDeingles.AdicionarAluno(p2);

cursoDeingles.ListarAlunos();

cursoDeingles.RemoverAluno(p2);
cursoDeingles.ListarAlunos();
