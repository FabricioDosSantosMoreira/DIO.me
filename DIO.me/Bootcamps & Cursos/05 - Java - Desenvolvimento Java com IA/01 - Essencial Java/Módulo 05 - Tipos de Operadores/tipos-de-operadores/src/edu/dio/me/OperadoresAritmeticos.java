package edu.dio.me;

public class OperadoresAritmeticos {

    // - - - - - > Operadores Aritméticos:
    //                 Em Java, operadores aritméticos são usados para realizar operações matemáticas básicas. 
    //
    // - - - - > Exemplos de Operadores Aritméticos:

    public static void main(String[] args) {
        System.out.println("\nExemplos de Operadores Aritméticos:");

        int x = 10; int y = 5;

        // - - - > Operador de adição (+):
        System.out.println("\nOperador aritmético de adição (+):");

        int resultadoAdicao = x + y;
        System.out.println("Resultado [x + y]: " + resultadoAdicao);


        // - - - > Operador de subtração (-):
        System.out.println("\nOperador aritmético de subtração (-):");
        
        int resultadoSubtracao = x - y;
        System.out.println("Resultado [x - y]: " + resultadoSubtracao);


        // - - - > Operador de multiplicação (*):
        System.out.println("\nOperador aritmético de multiplicação (*):");

        int resultadoMultiplicacao = x * y;    
        System.out.println("Resultado [x * y]: " + resultadoMultiplicacao);


        // - - - > Operador de divisão (/):
        System.out.println("\nOperador aritmético de divisão (/):");
        
        int resultadoDivisao = x / y;
        System.out.println("Resultado [x / y]: " + resultadoDivisao);


        // - - - > Operador de divisão inteira (/):
        System.out.println("\nOperador aritmético de divisão inteira (/):");

        int resultadoDivisaoInteira = x / y;
        System.out.println("Resultado [x / y]: " + resultadoDivisaoInteira);


        // - - - > Operador de resto ou módulo (%):
        System.out.println("\nOperador aritmético de resto ou módulo (%):");

        int resultadoModulo = x % y;
        System.out.println("Resultado [x % y]: " + resultadoModulo);


        // - - - > Operador de exponenciação (Math.pow()):
        System.out.println("\nOperador aritmético de exponenciação (Math.pow()):");
        
        double resultadoExponenciacao = Math.pow(x, y);
        System.out.println("Resultado [Math.pow(x, y)]: " + resultadoExponenciacao);
    }
}
