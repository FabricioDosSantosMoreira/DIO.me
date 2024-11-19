package edu.dio.me;

public class EstruturasCondicionais {

    // - - - - - > Estruturas Condicionais:
    //                 Em Java, As estruturas condicionais são usadas para tomar 
    //             decisões baseadas em condições. Elas permitem que diferentes 
    //             blocos de código sejam executados dependendo do resultado de  
    //             uma expressão booleana.

    public static void main(String[] args) {

        // - - - - > Exemplos de Estruturas Condicionais:
        System.out.println("\nExemplos de Estruturas Condicionais:");


        // - - - > Estrutura Condicional Simples:
        System.out.println("\nEstrutura Condicional Simples:");

        int x = 10;

        if (x > 0) {
            System.out.println("'x' é positivo!");
        }


        // - - - > Estrutura Condicional Composta:
        System.out.println("\nEstrutura Condicional Composta:");

        int y = -5;

        if (y > 0) {
            System.out.println("'y' é positivo!");
        } else {
            System.out.println("'y' é negativo ou zero!");
        }


        // - - - > Estrutura Condicional Encadeada:
        System.out.println("\nEstrutura Condicional Encadeada:");

        int z = 0;

        if (z > 0) {
            System.out.println("'z' é positivo!");
        } else if (z < 0) {
            System.out.println("'z' é negativo!");
        } else {
            System.out.println("'z' é zero!");
        }


        // - - - > Estrutura Condicional Ternária:
        System.out.println("\nEstrutura Condicional Ternária:");

        int a = 10;

        String resultado = (a > 0) ? "'a' é positivo!" : (a < 0) ? "'a' é negativo!" : "'a' é zero!";
        System.out.println(resultado);


        // - - - - > Estrutura Condicional Switch Case:
        System.out.println("\nEstrutura Condicional Switch Case:");

        int opcao = 3;
        String tamanho;

        switch (opcao) {
            case 1:
                tamanho = "pequeno";
                break;
            case 2:
                tamanho = "médio";
                break;
            case 3:
                tamanho = "grande";
                break;        
            default:
                tamanho = "padrão";
                break;
        }

        System.out.println(tamanho);
    }
}
