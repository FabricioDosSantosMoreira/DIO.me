package edu.dio.me;

public class ExemploDeConstantes {

    // Definindo Constantes:
    public static final String ESTADO = "RS";
    public static final int ANO_ATUAL = 2024;
    public static final double PI = 3.14159;

    public static void main(String[] args) {
    
        // Exemplo de Constantes:
        System.out.println("\nExemplo de Constantes:");

        System.out.println("Estado: " + ESTADO);
        System.out.println("Ano Atual: " + ANO_ATUAL);
        System.out.println("Valor de PI: " + PI);

        // Isto causará um erro de compilação, pois as constantes não podem ser alteradas
        // ANO_ATUAL = 2099;
    }
}
