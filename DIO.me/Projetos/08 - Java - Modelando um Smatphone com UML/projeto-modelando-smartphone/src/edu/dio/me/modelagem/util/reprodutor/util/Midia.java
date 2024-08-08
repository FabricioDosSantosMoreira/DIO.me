package edu.dio.me.modelagem.util.reprodutor.util;

public abstract class Midia {

    // Atributos da classe abstrata 'Midia'
    private String titulo;
    private double duracao;

    // Construtor da classe abstrata 'Midia'
    public Midia(String titulo, double duracao) {
        this.titulo = titulo;
        this.duracao = duracao;
    }

    // Método abstrato para exibir detalhes da mídia
    public abstract void exibirDetalhes();

    // Métodos 'getters' e 'setters' da classe abstrata 'Midia'
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public double getDuracao() {
        return duracao;
    }

    public void setDuracao(double duracao) {
        this.duracao = duracao;
    }
}
