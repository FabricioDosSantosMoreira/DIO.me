package edu.me.estruturas;

public class EstruturaCondicionalTernaria {
    
    public static void main(String[] args) {
        int numero = 10; // Exemplo de número   
        int nota = 5;

        String resultado_nota = nota >=7 ? "aprovado": nota >=5 && nota <7 ? "Recuperação" : "Reprovado";

        String resultado = (numero % 2 == 0) ? "Par" : "Ímpar";
        

        System.out.println("O número " + numero + " é " + resultado);
        System.out.println("A nota é: " + resultado_nota);
    }
}
