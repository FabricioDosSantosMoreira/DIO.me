package edu.dio.me;

public class ExemploDeVariaveis {

    public static void main(String[] args) {
    
        // Exemplo de Variáveis de Tipos Primitivos:
        System.out.println("\nExemplo de Variáveis de Tipos Primitivos:");

        // Variável do tipo inteiro (int):
        int idade = 19;
        System.out.println("Idade: " + idade);
    
        // Variável do tipo ponto flutuante (float):
        float altura = 1.85f;
        System.out.println("Altura: " + altura);

        // Variável do tipo caractere (char):
        char inicial = 'F';
        System.out.println("Inicial: " + inicial);

        // Variável do tipo booleano (boolean):
        boolean estudante = true;
        System.out.println("Estudante: " + estudante);


        // Exemplo de Variáveis de Tipos Referenciados:
        System.out.println("\nExemplo de Variáveis de Tipos Referenciados:");

        // Variável do tipo String:
        String nome = "Fabrício";
        System.out.println("Nome: " + nome);

        // Variável do tipo array (vetor):
        int[] numeros = {1, 2, 3, 4, 5};
        System.out.print("Números no array: ");
        for (int numero : numeros) {
            System.out.print(numero);
        }
    }
}
