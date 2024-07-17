package edu.me.aparelho.reprodutor.util;

public class Musica extends Midia {

    // Atributo da classe 'Midia'
    private String genero;

    // Construtor da classe 'Musica'
    public Musica(String titulo, double duracao, String genero) {
        super(titulo, duracao);
        this.genero = genero;
    }

    @Override
    public void exibirDetalhes() {
        System.out.println("Título: " + getTitulo());
        System.out.println("Duração: " + getDuracao() + " segundos");
        System.out.println("Gênero: " + genero);
    }

    // Getters e Setters da classe 'Midia'
    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

}
