// - - - - -> Tipos de Dados:

 
package edu.me.sintaxe;

public class TiposDeDados {

    public static void main(String[] args) {
        // Tipos primitivos
        byte byteVar = 127;             // Byte - 8 bits
        short shortVar = 32000;         // Short - 16 bits
        int intVar = 2147483647;        // Int - 32 bits
        long longVar = 9223372036854775807L; // Long - 64 bits (o sufixo 'L' indica que é um longo)

        float floatVar = 3.14f;         // Float - 32 bits (o sufixo 'f' indica que é um float)
        double doubleVar = 3.14159;     // Double - 64 bits (não requer sufixo)

        boolean booleanVar = true;      // Booleano - true ou false

        char charVar = 'A';             // Char - caractere Unicode (16 bits)

        String str = "Olá, mundo!";
        int[] array = {1, 2, 3, 4, 5};


        // Saída dos valores
        System.out.println("Tipos de dados em Java:");
        System.out.println("Byte: " + byteVar);
        System.out.println("Short: " + shortVar);
        System.out.println("Int: " + intVar);
        System.out.println("Long: " + longVar);
        System.out.println("Float: " + floatVar);
        System.out.println("Double: " + doubleVar);
        System.out.println("Boolean: " + booleanVar);
        System.out.println("Char: " + charVar);
    }
}