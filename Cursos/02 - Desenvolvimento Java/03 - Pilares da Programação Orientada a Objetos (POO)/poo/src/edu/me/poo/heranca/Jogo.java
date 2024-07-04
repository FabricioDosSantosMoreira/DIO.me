package edu.me.poo.heranca;


public abstract class Jogo {

    // Atributos
    protected String nome;
    protected int nrJogadores;

    // Método contrutor completo
    public Jogo(String nome, int nrJogadores) {
        this.nome = nome;
        this.nrJogadores = nrJogadores;
    }

    // Métodos Getters e Setters
    public String getNome() {
        return nome;
    }
    public int getNrJogadores() {
        return nrJogadores;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setNrJogadores(int nrJogadores) {
        this.nrJogadores = nrJogadores;
    }

    // OBS: poderia usar 'final', porém não teria como fazer '@Override' nas classes filhas
    public void infoJogo() {
        System.out.println(
            "\nNome: " + nome +
            "\nN° Jogadores: " + nrJogadores
        );
    }

    public void jogar() {
    	System.out.println("\nVocê está jogando!");
    }
}