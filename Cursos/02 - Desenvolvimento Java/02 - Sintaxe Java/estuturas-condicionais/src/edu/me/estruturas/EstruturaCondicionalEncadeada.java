package edu.me.estruturas;

public class EstruturaCondicionalEncadeada {
    
    public static void main(String[] args) {
        int pontuacao = 85; // Exemplo de pontuação
        
        if (pontuacao >= 90) {
            System.out.println("Nota A");
        } else if (pontuacao >= 80) {
            System.out.println("Nota B");
        } else if (pontuacao >= 70) {
            System.out.println("Nota C");
        } else if (pontuacao >= 60) {
            System.out.println("Nota D");
        } else {
            System.out.println("Nota F");
        }
    }
}
