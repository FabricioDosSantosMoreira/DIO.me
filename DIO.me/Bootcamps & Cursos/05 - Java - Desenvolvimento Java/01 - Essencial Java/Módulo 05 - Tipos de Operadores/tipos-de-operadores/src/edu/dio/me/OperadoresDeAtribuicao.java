package edu.dio.me;

public class OperadoresDeAtribuicao {

    // - - - - - > Operadores de Atribuição:
    //                 Em Java, operadores de atribuição são usados para atribuir valores a variáveis.
    //
    // - - - - > Exemplos de Operadores Atribuição:

    public static void main(String[] args) {
        System.out.println("\nExemplos de Operadores de Atribuição:");

        // Operador de atribuição (=):
        System.out.println("\nOperador de atribuição (=):");

        int x = 5;
        System.out.println("Resultado [x = 5]: " + x);


        // Operador de atribuição com adição (+=):
        System.out.println("\nOperador de atribuição com adição (+=):");

        x += 5; // Equivalente a x = x + 5;    
        System.out.println("Resultado [x += 5]: " + x);


        // Operador de atribuição com subtração (-=):
        System.out.println("\nOperador de atribuição com subtração (-=):");

        x -= 5; // Equivalente a x = x - 5;
        System.out.println("Resultado [x -= 5]: " + x);


        // Operador de atribuição com multiplicação (*=):
        System.out.println("\nOperador de atribuição com multiplicação (*=):");

        x *= 5; // Equivalente a x = x * 5;
        System.out.println("Resultado [x *= 5]: " + x);


        // Operador de atribuição com divisão (/=):
        System.out.println("\nOperador de atribuição com divisão (/=):");

        x /= 5; // Equivalente a x = x / 5;
        System.out.println("Resultado [x /= 5]: " + x);


        // Operador de atribuição com resto (%=):
        System.out.println("\nOperador de atribuição com resto (%=):");
        
        x %= 5; // Equivalente a x = x % 5;
        System.out.println("Resultado [x %= 5]: " + x);
    }
}
