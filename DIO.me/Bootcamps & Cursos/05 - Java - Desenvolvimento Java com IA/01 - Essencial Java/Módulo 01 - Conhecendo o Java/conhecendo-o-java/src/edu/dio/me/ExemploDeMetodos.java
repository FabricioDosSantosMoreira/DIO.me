package edu.dio.me;

public class ExemploDeMetodos {

    public static void main(String[] args) {

        // Criando uma instância da classe 'Pessoa'
        Pessoa pessoa = new Pessoa("Fabrício", 2005);

        // Acessando o método 'apresentar()' da classe 'Pessoa'
        pessoa.apresentar();
    }
}


class Pessoa {

    // Atributos da classe 'Pessoa'
    private String nome;
    private int anoNascimento;

    // Construtor da classe 'Pessoa'
    public Pessoa(String nome, int anoNascimento) {
        this.nome = nome;
        this.anoNascimento = anoNascimento;
        System.out.println("Objeto da classe 'Pessoa' criado!");
    }

    // Método para apresentar informações da pessoa
    public void apresentar() {
        System.out.println("Olá! Meu nome é " + nome + " e tenho " + this.calcularIdade() + " anos.");
    }

    // Método para calcular a idade
    public int calcularIdade() {
        int anoAtual = java.util.Calendar.getInstance().get(java.util.Calendar.YEAR);
        return anoAtual - this.getAnoNascimento();
    }

    // Método para obter o nome
    public String getNome() {
        return this.nome;
    }

    // Método para obter o ano de nascimento
    public int getAnoNascimento() {
        return this.anoNascimento;
    }
}
