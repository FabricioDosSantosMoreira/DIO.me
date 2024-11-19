package edu.dio.me;

import java.util.Scanner;

public class EntradaSaidaDados {

    public static void main(String[] args) {

        // Exemplo de Entrada de Dados:
        System.out.println("\nExemplo de Entrada de Dados:");
        
        // Criando um objeto Scanner para ler dados do console
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();


        // Exemplo de Saída de Dados:
        System.out.println("\nExemplo de Saída de Dados:");

        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);


        // Exemplo de Formatação de Saída de Dados com 'String.format()':
        System.out.println("\nExemplo de Formatação de Saída de Dados com 'String.format()':");

        String mensagem = String.format("Olá %s, você tem %d anos.", nome, idade);
        System.out.println(mensagem);


        // Exemplo de Formatação de Saída de Dados com 'printf()':
        System.out.println("\nExemplo de Formatação de Saída de Dados com 'printf()':");

        System.out.printf("Olá %s, você tem %d anos.", nome, idade);


        // Fechando o Scanner
        scanner.close();
    }
}
