package edu.dio.me;

public class OperadoresDeComparacao {

    // - - - - - > Operadores de Comparação:
    //                 Em Java, operadores de comparação são utilizados para comparar dois valores e 
    //             retornar um valor booleano (true ou false) dependendo do resultado da comparação. 
    //
    // - - - - > Exemplos de Operadores de Comparação:

    public static void main(String[] args) {
        System.out.println("\nExemplos de Operadores de Comparação:");

        int a = 10;
        int b = 20;

        // - - - > Operador de comparação de igualdade (==):
        System.out.println("\nOperador de comparação de igualdade (==):");

        boolean resultadoIgualdade = (a == b);
        System.out.println("Resultado [a == b]: " + resultadoIgualdade);


        // - - - > Operador de comparação de diferença (!=):
        System.out.println("\nOperador de comparação de diferença (!=):");

        boolean resultadoDiferenca = (a != b);
        System.out.println("Resultado [a != b]: " + resultadoDiferenca);


        // - - - > Operador de comparação maior que (>):
        System.out.println("\nOperador de comparação maior que (>):");
        
        boolean resultadoMaiorQue = (a > b);
        System.out.println("Resultado [a > b]: " + resultadoMaiorQue);


        // - - - > Operador de comparação menor que (<):
        System.out.println("\nOperador de comparação menor que (<):");

        boolean resultadoMenorQue = (a < b);
        System.out.println("Resultado [a < b]: " + resultadoMenorQue);


        // - - - > Operador de comparação maior ou igual a (>=):
        System.out.println("\nOperador de comparação maior ou igual a (>=):");

        boolean resultadoMaiorOuIgual = (a >= b);
        System.out.println("Resultado [a >= b]: " + resultadoMaiorOuIgual);


        // - - - > Operador de comparação menor ou igual a (<=):
        System.out.println("\nOperador de comparação menor ou igual a (<=):");

        boolean resultadoMenorOuIgual = (a <= b);
        System.out.println("Resultado [a <= b]: " + resultadoMenorOuIgual);
    }
}
