package edu.dio.me;

public class Pessoa {

    // Atributos privados da classe 'Pessoa'
    private String nome;
    private int idade;

    // Método construtor da classe 'Pessoa'
    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    // Métodos 'getters' e 'setters' da classe 'Pessoa'
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        if (idade > 0) {
            this.idade = idade;
        }
    }
}
