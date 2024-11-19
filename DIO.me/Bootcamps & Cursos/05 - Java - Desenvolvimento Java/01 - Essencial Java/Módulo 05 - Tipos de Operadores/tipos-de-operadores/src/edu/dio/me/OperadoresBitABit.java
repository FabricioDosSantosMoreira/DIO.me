package edu.dio.me;

public class OperadoresBitABit {

    // - - - - - > Operadores Bit a Bit:
    //                 Em Java, operadores bit a bit são usados para realizar operações em nível 
    //             de bits. Eles operam diretamente nos bits de números inteiros e incluem 'AND'
    //             'OR', 'XOR', 'negação' e 'deslocamento' de bits.
    //
    // - - - - > Exemplos de Operadores Bit a Bit:

    public static void main(String[] args) {
        System.out.println("Exemplos de Operadores Bit a Bit:");

        int x = 12; // 00001100 em binário
        int y = 7;  // 00000111 em binário

        // - - - > Operador bit a bit AND (&):
        System.out.println("\nOperador bit a bit AND (&):");

        int resultado = x & y;
        System.out.println("Resultado [x & y]: " + resultado); // 00000100 em binário = 4


        // - - - > Operador bit a bit OR (|):
        System.out.println("\nOperador bit a bit OR (|):");

        resultado = x | y;
        System.out.println("Resultado [x | y]: " + resultado); // 00001111 em binário = 15


        // - - - > Operador bit a bit XOR (^):
        System.out.println("\nOperador bit a bit XOR (^):");

        resultado = x ^ y;
        System.out.println("Resultado [x ^ y]: " + resultado); // 00001011 em binário = 11


        // - - - > Operador bit a bit NOT (~):
        System.out.println("\nOperador bit a bit NOT (~):");

        resultado = ~x;
        System.out.println("Resultado [~x]: " + resultado); // -00010001 em binário (o resultado depende da implementação do Java)


        // - - - > Operador de Deslocamento para a Esquerda (<<):
        System.out.println("\nOperador de Deslocamento para a Esquerda (<<):");

        resultado = x << 2;
        System.out.println("Resultado [x << 2]: " + resultado); // 00110000 em binário = 48


        // - - - > Operador de Deslocamento para a Direita (>>):
        System.out.println("\nOperador de Deslocamento para a Direita (>>):");

        resultado = x >> 2;
        System.out.println("Resultado [x >> 2]: " + resultado); // 00000011 em binário = 3


        // - - - > Operador de Deslocamento para a Direita com Preenchimento de 0 (>>>):
        System.out.println("\nOperador de Deslocamento para a Direita com Preenchimento de 0 (>>>):");

        resultado = x >>> 2;
        System.out.println("Resultado [x >>> 2]: " + resultado); // 00000011 em binário = 3
    }
}
