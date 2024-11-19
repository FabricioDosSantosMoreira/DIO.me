// ├───────> Exercício - Lista de Alunos:
// │             Crie uma classe chamada 'GerenciadorAlunos' que irá lidar com uma lista de alunos. 
// │         Cada aluno terá atributos como nome, matrícula e nota. 
// │         Implemente os seguintes métodos:
// │
// │             * adicionarAluno(String nome, Long matricula, double media):
// │                   Adiciona um aluno ao conjunto.
// │
// │             * removerAluno(long matricula):
// │                   Remove um aluno ao conjunto a partir da matricula, se estiver presente.
// │
// │             * exibirAlunosPorNome():
// │                   Exibe todos os alunos do conjunto em ordem alfabética pelo nome.
// │
// │             * exibirAlunosPorMedia():
// │                   Exibe todos os alunos do conjunto em ordem crescente de media.
// │
// │             * exibirAlunos():
// │                   Exibe todos os alunos do conjunto.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.set.Ordenacao.ListaDeAlunos;

public class Main {

    public static void main(String[] args) {

        // Instânciando um objeto da classe 'GerenciadorAlunos'
        GerenciadorAlunos alunos = new GerenciadorAlunos();

        // Adicionando alunos
        alunos.adicionarAluno("Aluno A", 1000L, 6.0);
        alunos.adicionarAluno("Aluno D", 1001L, 7.9);
        alunos.adicionarAluno("Aluno C", 1002L, 4.6);
        alunos.adicionarAluno("Aluno K", 1003L, 9.0);
        alunos.adicionarAluno("Aluno F", 1004L, 10.0);

        alunos.removerAluno(1000L);

        System.out.println("\nExibindo os alunos:");
        alunos.exibirAlunos();

        System.out.println("\nExibindo os alunos por nome:");
        alunos.exibirAlunosPorNome();

        System.out.println("\nExibindo os alunos por media:");
        alunos.exibirAlunosPorMedia();
    }
}
