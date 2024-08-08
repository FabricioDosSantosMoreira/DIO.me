package edu.dio.me.exercicios.set.Ordenacao.ListaDeAlunos;

import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class GerenciadorAlunos {

    // Atributo da classe 'GerenciadorAlunos'
    private Set<Aluno> alunos;

    // Construtor da classe 'GerenciadorAlunos'
    public GerenciadorAlunos() {
        this.alunos = new HashSet<>();
    }

    // Métodos da classe 'GerenciadorAlunos'
    public void adicionarAluno(String nome, Long matricula, double media) { 
        this.alunos.add(new Aluno(nome, matricula, media));
    }

    public void removerAluno(long matricula) {
        if (!this.alunos.isEmpty()) {
            for (Aluno a : this.alunos) {
                if (a.getMatricula().equals(matricula))  {
                    this.alunos.remove(a);
                    System.out.println("\nAluno removido!");
                    break;
                }
            }
        } else {
            System.out.println("\nNenhum aluno!");
        }
    }

    public void exibirAlunosPorNome() {
        // Organiza por nome. O TreeSet detecta o método 'compareTo' de 'Aluno'
        Set<Aluno> AlunosPorNome = new TreeSet<>(this.alunos);

        if (!AlunosPorNome.isEmpty()) {
            for (Aluno a : AlunosPorNome) {
                System.out.println("Aluno: "+ a); 
            }
        } else {
            System.out.println("\nNenhum aluno!");
        }
    }

    public void exibirAlunosPorMedia() {
        Set<Aluno> alunosPorNota = new TreeSet<>(new ComparatorPorMedia());
        alunosPorNota.addAll(this.alunos);

        if (!alunosPorNota.isEmpty()) {
            for (Aluno a : alunosPorNota) {
                System.out.println("Aluno: "+ a); 
            }
        } else {
            System.out.println("\nNenhum aluno!");
        }
    }

    public void exibirAlunos() {
        if (!this.alunos.isEmpty()) {
            for (Aluno a : this.alunos) {
                System.out.println("Aluno: "+ a); 
            }
        } else {
            System.out.println("\nNenhum aluno!");
        }
    }
}
 