package edu.me.poo.encapsulamento;


/* Encapsulamento é um dos princípios fundamentais da programação orientada 
a objetos (POO) em Java. Ele é usado para proteger os dados de uma classe, 
garantindo que o acesso a esses dados seja controlado e seguro. O encapsulamento 
é realizado através do uso de modificadores de acesso (como private, protected, e public) 
e métodos getter e setter.*/


//Os campos nome e idade são declarados como private, o que significa que eles não podem ser 
// acessados diretamente de fora da classe Pessoa.

//Os métodos getNome e setNome, getIdade e setIdade são usados para acessar e modificar os 
//campos privados. Estes métodos são chamados de métodos getter e setter.

//A classe Main cria um objeto da classe Pessoa e usa os métodos getter e setter para acessar 
//e modificar os campos nome e idade.

public class Pessoa {
    // Campos privados
    private String nome;
    private int idade;

    // Construtor
    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    // Método getter para o nome
    public String getNome() {
        return nome;
    }

    // Método setter para o nome
    public void setNome(String nome) {
        this.nome = nome;
    }

    // Método getter para a idade
    public int getIdade() {
        return idade;
    }

    // Método setter para a idade
    public void setIdade(int idade) {
        if (idade > 0) { // Validação simples
            this.idade = idade;
        }
    }

    // Método para exibir informações da pessoa
    public void exibirInfo() {
        System.out.println("Nome: " + nome + ", Idade: " + idade);
    }
}

