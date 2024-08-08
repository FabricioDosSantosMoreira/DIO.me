package edu.dio.me.exercicios.list.Basico.CarrinhoDeCompras;

public class Item {

    // Atributos da classe 'Item'
    private String nome;
    private double preco;
    private int quantidade;

    // Método construtor da classe 'Item'
    public Item(String nome, double preco, int quantidade) {
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    // Métodos 'getters' e 'setters' da classe 'Item'
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }
}
