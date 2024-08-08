package edu.dio.me;

public class EstruturasDeExcecao {
    
    // - - - - - > Estruturas de Exceção:
    //                 Em Java, as estruturas de exceções são usadas para lidar 
    //             com erros e situações inesperadas que podem ocorrer durante 
    //             a execução de um programa. As exceções podem ser tratadas 
    //             blocos try-catch e lançadas usando a palavra-chave throw.

    public static void main(String[] args) {
        
        // - - - - > Exemplos de Estruturas de Exceção:
        System.out.println("\nExemplos de Estruturas de Exceção:");


        // - - - > Estrutura de Exceção:
        System.out.println("\nEstrutura de Exceção:");

        try {
            int resultado = 10 / 0; // Isso causará uma ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Erro: " + e.getMessage());
        } finally {
        System.out.println("Bloco finally executado!");
        }


        // - - - > Lançamento de Exceção:
        System.out.println("\nLançamento de Exceção:");
        try {
            boolean valido = false;
            if (!valido) {
                throw new Exception("Inválido");
            }
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }
}
