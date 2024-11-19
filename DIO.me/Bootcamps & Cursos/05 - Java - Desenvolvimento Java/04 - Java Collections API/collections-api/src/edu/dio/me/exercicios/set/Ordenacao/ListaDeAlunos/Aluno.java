package edu.dio.me.exercicios.set.Ordenacao.ListaDeAlunos;

import java.util.Comparator;
import java.util.Objects;

public class Aluno implements Comparable<Aluno> {

    // Atributos da classe 'Aluno'
    private String nome;
    private Long matricula;
    private double media;

    // Método construtor da classe 'Aluno'
    public Aluno(String nome, Long matricula, double media) {
        this.nome = nome;
        this.matricula = matricula;
        this.media = media;
    }

    // Método 'equals()' da classe 'Aluno'
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Aluno aluno)) return false;
        return Objects.equals(getMatricula(), aluno.getMatricula());
    }

    // Método 'hashCode()' da classe 'Aluno'
    @Override
    public int hashCode() {
        return Objects.hash(getMatricula());
    }

    // Método 'compareTo()' da classe 'Aluno'
    @Override
    public int compareTo(Aluno aluno) {
        return this.nome.compareTo(aluno.getNome());
    }

    // Método 'toString()' da classe 'Aluno'
    @Override
    public String toString() {
        return "Aluno [nome=" + nome + ", matricula=" + matricula + ", media=" + media + "]";
    }

    // Métodos 'getters' e 'setters' da classe 'Aluno'
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Long getMatricula() {
        return matricula;
    }
    
    public void setMatricula(Long matricula) {
        this.matricula = matricula;
    }

    public double getMedia() {
        return media;
    }

    public void setMedia(double media) {
        this.media = media;
    }
}


class ComparatorPorMedia implements Comparator<Aluno>{

    @Override
    public int compare(Aluno a1, Aluno a2) {
        return Double.compare(a1.getMedia(), a2.getMedia());
    }
}
