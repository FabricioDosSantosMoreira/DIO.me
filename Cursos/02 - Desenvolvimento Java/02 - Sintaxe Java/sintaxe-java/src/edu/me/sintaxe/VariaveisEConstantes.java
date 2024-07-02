package edu.me.sintaxe;

public class VariaveisEConstantes {
    // Exemplo de variáveis
    int variavelInteira = 10;
    double variavelDouble = 3.14;
    String variavelString = "Olá, mundo!";
    
    // Exemplo de constantes
    static final int CONSTANTE_INT = 100;
    static final double CONSTANTE_DOUBLE = 2.71828;
    static final String CONSTANTE_STRING = "Esta é uma constante";

    public static void main(String[] args) {
        VariaveisEConstantes exemplo = new VariaveisEConstantes();

        // Acessando variáveis
        System.out.println("Valor da variável inteira: " + exemplo.variavelInteira);
        System.out.println("Valor da variável double: " + exemplo.variavelDouble);
        System.out.println("Valor da variável string: " + exemplo.variavelString);

        // Acessando constantes
        System.out.println("Valor da constante inteira: " + CONSTANTE_INT);
        System.out.println("Valor da constante double: " + CONSTANTE_DOUBLE);
        System.out.println("Valor da constante string: " + CONSTANTE_STRING);

        // Tentativa de modificação de uma constante (irá gerar erro)
        // CONSTANTE_INT = 200; // Erro: cannot assign a value to final variable CONSTANTE_INT
    }
}
