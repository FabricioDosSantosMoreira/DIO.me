package edu.dio.me;

// - - - - - > Tipos de Dados em Java:
//                 Em Java, os tipos de dados podem ser classificados em primitivos e não primitivos.
//             Os tipos primitivos incluem: byte, short, int, long, float, double, char e boolean. 
//             Os tipos não primitivos (ou referência) incluem: String, Arrays, entre outros.

public class TiposDeDados {
    
    public static void main(String[] args) {
        
        // - - - - > Exemplo de Tipos de Dados Primitivos:
        System.out.println("\nExemplo de Tipos de Dados Primitivos:");

        // - - - > Tipo byte:
        byte byteVar = 100;
        System.out.println("Tipo byte:");
        System.out.println("Valor de 'byteVar': " + byteVar);

        // - - - > Tipo short:
        short shortVar = 10000;
        System.out.println("\nTipo short:");
        System.out.println("Valor de 'shortVar': " + shortVar);

        // - - - > Tipo int:
        int intVar = 100000;
        System.out.println("\nTipo int:");
        System.out.println("Valor de 'intVar': " + intVar);

        // - - - > Tipo long:
        long longVar = 100000L;
        System.out.println("\nTipo long:");
        System.out.println("Valor de 'longVar': " + longVar);

        // - - - > Tipo float:
        float floatVar = 10.5f;
        System.out.println("\nTipo float:");
        System.out.println("Valor de 'floatVar': " + floatVar);

        // - - - > Tipo double:
        double doubleVar = 20.99;
        System.out.println("\nTipo double:");
        System.out.println("Valor de 'doubleVar': " + doubleVar);

        // - - - > Tipo char:
        char charVar = 'A';
        System.out.println("\nTipo char:");
        System.out.println("Valor de 'c'harVar': " + charVar);

        // - - - > Tipo boolean:
        boolean booleanVar = true;
        System.out.println("\nTipo boolean:");
        System.out.println("Valor de 'booleanVar': " + booleanVar);


        // - - - - > Exemplo de Tipos de Dados Não Primitivos:
        System.out.println("\nExemplo de Tipos de Dados Não Primitivos:");

        // - - - > Tipo String:
        String stringVar = "Olá, mundo!";
        System.out.println("\nTipo String:");
        System.out.println("Valor de 'stringVar': " + stringVar);

        // - - - > Tipo Array:
        int[] arrayVar = {1, 2, 3, 4, 5};
        System.out.println("\nTipo Array:");
        System.out.print("Valores de 'arrayVar': ");
        for (int num : arrayVar) {
            System.out.print(num);
        }
    }
}
