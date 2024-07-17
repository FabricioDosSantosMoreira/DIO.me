package edu.me.aparelho.reprodutor.util;

public class Video extends Midia {

    private String resolucao;

    public Video(String titulo, double duracao, String resolucao) {
        super(titulo, duracao);
        this.resolucao = resolucao;
    }

    public String getResolucao() {
        return resolucao;
    }

    public void setResolucao(String resolucao) {
        this.resolucao = resolucao;
    }

    @Override
    public void exibirDetalhes() {
        System.out.println("Título: " + getTitulo());
        System.out.println("Duração: " + getDuracao() + " segundos");
        System.out.println("Resolução: " + resolucao);
    }
}
