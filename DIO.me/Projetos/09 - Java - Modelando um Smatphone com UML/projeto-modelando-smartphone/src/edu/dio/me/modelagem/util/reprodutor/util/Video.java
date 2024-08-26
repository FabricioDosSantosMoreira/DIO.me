package edu.dio.me.modelagem.util.reprodutor.util;

public class Video extends Midia {

    // Atributo da classe 'Video'
    private String resolucao;

    // Construtor da classe 'Video'
    public Video(String titulo, double duracao, String resolucao) {
        super(titulo, duracao);
        this.resolucao = resolucao;
    }

    // Método para exibir detalhes do video
    @Override
    public void exibirDetalhes() {
        System.out.println("Título: " + getTitulo());
        System.out.println("Duração: " + getDuracao() + " segundos");
        System.out.println("Resolução: " + resolucao);
    }

    // Métodos 'getters' e 'setters' da classe 'Video'
    public String getResolucao() {
        return resolucao;
    }

    public void setResolucao(String resolucao) {
        this.resolucao = resolucao;
    }
}
