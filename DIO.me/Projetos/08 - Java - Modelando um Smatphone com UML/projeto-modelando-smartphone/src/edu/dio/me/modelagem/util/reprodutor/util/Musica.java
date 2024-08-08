package edu.dio.me.modelagem.util.reprodutor.util;

public class Musica extends Midia {

    // Atributo da classe 'Musica'
    private String genero;

    // Construtor da classe 'Musica'
    public Musica(String titulo, double duracao, String genero) {
        super(titulo, duracao);
        this.genero = genero;
    }

    // Método para exibir detalhes da musica
    @Override
    public void exibirDetalhes() {
        System.out.println("Título: " + getTitulo());
        System.out.println("Duração: " + getDuracao() + " segundos");
        System.out.println("Gênero: " + genero);
    }

    // Métodos 'getters' e 'setters' da classe 'Musica'
    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }
}
