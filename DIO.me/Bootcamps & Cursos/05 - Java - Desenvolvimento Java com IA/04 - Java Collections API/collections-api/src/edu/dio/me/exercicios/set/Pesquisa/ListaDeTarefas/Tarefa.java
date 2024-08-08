package edu.dio.me.exercicios.set.Pesquisa.ListaDeTarefas;

public class Tarefa {

    // Atributo da classe 'Tarefa'
    private String descricao;
    private boolean concluida;
    
    // Método construtor da classe 'Tarefa'
    public Tarefa(String descricao) {
        this.descricao = descricao;
        this.concluida = false;
    }

    // Método 'toString()' da classe 'Tarefa'
    @Override
    public String toString() {
        return "Tarefa [descricao=" + descricao + ", concluida=" + concluida + "]";
    }

    // Métodos 'getters' e 'setters' da classe 'Tarefa'
    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public boolean isConcluida() {
        return concluida;
    }

    public void setConcluida(boolean concluida) {
        this.concluida = concluida;
    }
}
