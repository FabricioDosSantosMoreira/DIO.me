package edu.dio.me;

public class EstruturasDeRepeticao {

    // - - - - - > Estruturas de Repetição:
    //                 Em Java, As estruturas de repetição São usadas para repetir
    //             um trecho de código um determinado número de vezes. Esse número
    //             pode ser conhecido previamente ou determinado através de uma 
    //             expressão lógica.

    public static void main(String[] args) {
        
        // - - - - > Exemplos de Estruturas de Repetição:
        System.out.println("\nExemplos de Estruturas de Repetição:");


        // - - - > Exemplo de Estrutura de Repetição 'for':
        System.out.println("\nExemplo de Estrutura de Repetição 'for':");

        for (int i = 0; i < 5; i++) {
            System.out.println("i: " + i);
        }


        // - - - > Exemplo de Estrutura de Repetição 'for each':
        System.out.println("\nExemplo de Estrutura de Repetição 'for each':");

        int[] numeros = {0, 1, 2, 3, 4};
        for (int n : numeros) {
            System.out.println("numero = " + n);
        }


        // - - - > Exemplo de Estrutura de Repetição 'while':
        System.out.println("\nExemplo de Estrutura de Repetição 'while':");

        int contador = 0;
        while (contador < 5) {
            System.out.println("contador = " + contador);
            contador++;
        }


        // - - - > Exemplo de Estrutura de Repetição 'do-while':
        System.out.println("\nExemplo de Estrutura de Repetição 'do-while':");

        int numero = 0;
        do {
            System.out.println("numero = " + numero);
            numero++;
        } while (numero < 5);
    }
}
