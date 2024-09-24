using ClassesAbstratas.Models;

ContaCorrente contaCorrente = new();

contaCorrente.Creditar(2000);
contaCorrente.ExibirSaldo();




// Construtor por Herança
Aluno aluno = new Aluno("Aluno");
aluno.Idade = 15;
aluno.Nota = 8;

aluno.Apresentar();

Professor professor = new Professor("Professor");
professor.Idade = 60;
professor.Salario = 2000;

professor.Apresentar();