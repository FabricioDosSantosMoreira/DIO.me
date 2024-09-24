using Polimorfismo.Models;

Aluno aluno = new Aluno();
aluno.Nome = "Aluno";
aluno.Idade = 15;
aluno.Nota = 8;

aluno.Apresentar();

Professor professor = new Professor();
professor.Nome = "Professor";
professor.Idade = 60;
professor.Salario = 2000;

// Polimorfismo em tempo de execução
professor.Apresentar();

// Polimorfismo em tempo de compilação
professor.Apresentar(esconderSalario: true);