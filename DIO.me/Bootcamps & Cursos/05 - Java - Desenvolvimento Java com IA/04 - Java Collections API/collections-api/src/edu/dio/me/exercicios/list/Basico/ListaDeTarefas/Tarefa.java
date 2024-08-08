package edu.dio.me.exercicios.list.Basico.ListaDeTarefas;

public class Tarefa {

    // Atributo da classe 'Tarefa'
    private String descricao;
    
    // Método construtor da classe 'Tarefa'
    public Tarefa(String descricao) {
        this.descricao = descricao;
    }

    // Métodos 'getters' e 'setters' da classe 'Tarefa'
    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }    
}
