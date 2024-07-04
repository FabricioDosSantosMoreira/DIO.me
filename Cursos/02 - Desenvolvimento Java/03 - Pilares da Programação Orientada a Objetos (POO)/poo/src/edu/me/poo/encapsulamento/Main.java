package edu.me.poo.encapsulamento;

public class Main {
    public static void main(String[] args) {
        // Criando um objeto da classe Pessoa
        Pessoa p = new Pessoa("João", 30);

        // Acessando e modificando os campos usando os métodos getter e setter
        p.setNome("Carlos");
        p.setIdade(35);

        // Exibindo as informações
        p.exibirInfo();
    }
}
