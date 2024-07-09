package SetInterface.Exercicios.Pesquisa.AgendaDeContatos;

import java.util.Objects;


public class Contato {

    // Atributos da classe 'Contato'
    private String nome;
    private int numero;

    // Construtor da classe 'Contato'
    public Contato(String nome, int numero) {
        this.nome = nome;
        this.numero = numero;
    }

    // Método 'toString' da classe 'Convidado'
    @Override
    public String toString() {
        return "Contato [nome=" + nome + ", numero=" + numero + "]";
    }

    // Método 'hashCode' da classe 'Convidado'
    @Override
    public int hashCode() {
        return Objects.hash(getNome());
    }

    // Método 'equals' da classe 'Convidado'
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Contato contato)) return false;
        return getNome() == contato.getNome();
    }

    // Getters e Setters da classe 'Contato'
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
