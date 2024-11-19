package edu.dio.me.exercicios.set.Pesquisa.AgendaDeContatos;

import java.util.Objects;

public class Contato {

    // Atributos da classe 'Contato'
    private String nome;
    private int numero;

    // Método construtor da classe 'Contato'
    public Contato(String nome, int numero) {
        this.nome = nome;
        this.numero = numero;
    }

    // Método 'toString()' da classe 'Contato'
    @Override
    public String toString() {
        return "Contato [nome=" + nome + ", numero=" + numero + "]";
    }

    // Método 'hashCode()' da classe 'Contato'
    @Override
    public int hashCode() {
        return Objects.hash(getNome());
    }

    // Método 'equals()' da classe 'Contato'
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Contato contato)) return false;
        return getNome() == contato.getNome();
    }

    // Métodos 'getters' e 'setters' da classe 'Contato'
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }
}
