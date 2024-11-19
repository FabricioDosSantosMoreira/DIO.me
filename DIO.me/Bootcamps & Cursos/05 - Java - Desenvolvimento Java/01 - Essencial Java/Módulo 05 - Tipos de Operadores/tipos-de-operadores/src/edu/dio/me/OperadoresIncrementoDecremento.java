package edu.dio.me;

public class OperadoresIncrementoDecremento {

    // - - - - - > Operadores de Incremento e Decremento:
    //                 Em Java, os operadores de incremento (++) e decremento (--) são utilizados para 
    //             aumentar ou diminuir o valor de uma variável em 1, respectivamente. Eles podem ser 
    //             usados forma prefixada (antes da variável) ou sufixada (depois da variável).
    //
    // - - - - > Exemplos de Operadores de Incremento e Decremento:

    public static void main(String[] args) {
        System.out.println("\nExemplos de Operadores de Incremento e Decremento:");

        int x = 10;
        int y = 5;

        // - - - > Operador de incremento (++) prefixado:
        System.out.println("\nOperador de incremento (++) prefixado:");

        System.out.println("Antes do incremento: x = " + x);
        int resultadoPrefixado = ++x;
        System.out.println("Depois do incremento: x = " + resultadoPrefixado);

        // - - - > Operador de incremento (++) sufixado:
        System.out.println("\nOperador de incremento (++) sufixado:");

        System.out.println("Antes do incremento: y = " + y);
        int resultadoSufixado = y++;
        System.out.println("Depois do incremento: y = " + y);
        System.out.println("Resultado do incremento sufixado: " + resultadoSufixado);

        // - - - > Operador de decremento (--) prefixado:
        System.out.println("\nOperador de decremento (--) prefixado:");

        System.out.println("Antes do decremento: x = " + x);
        int resultadoDecrementoPrefixado = --x;
        System.out.println("Depois do decremento: x = " + resultadoDecrementoPrefixado);

        // - - - > Operador de decremento (--) sufixado:
        System.out.println("\nOperador de decremento (--) sufixado:");

        System.out.println("Antes do decremento: y = " + y);
        int resultadoDecrementoSufixado = y--;
        System.out.println("Depois do decremento: y = " + y);
        System.out.println("Resultado do decremento sufixado: " + resultadoDecrementoSufixado);
    }
}
