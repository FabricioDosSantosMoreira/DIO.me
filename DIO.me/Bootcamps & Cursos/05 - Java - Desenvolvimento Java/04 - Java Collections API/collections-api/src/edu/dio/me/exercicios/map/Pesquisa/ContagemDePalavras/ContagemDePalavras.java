package edu.dio.me.exercicios.map.Pesquisa.ContagemDePalavras;

import java.util.HashMap;
import java.util.Map;

public class ContagemDePalavras {

    // Atributo da classe 'ContagemDePalavras'
    private Map<String, Integer> palavras;

    // Método construtor da classe 'ContagemDePalavras'
    public ContagemDePalavras() {
        this.palavras = new HashMap<>();
    }

    // Métodos da classe 'ContagemDePalavras'
    public void adicionarPalavra(String palavra, Integer contagem) {
        this.palavras.put(palavra, contagem);
    }

    public void removerPalavra(String palavra) {
        if(!this.palavras.isEmpty()) {
            this.palavras.remove(palavra);
        } else {
            System.out.println("\nNenhuma palavra!");
        }
    }

    public void exibirContagemPalavras() {
        if(!this.palavras.isEmpty()) {
            for (Map.Entry<String, Integer> entry : this.palavras.entrySet()) {
                    System.out.println("| Palavra: " + entry.getKey() + ", contagem: " + entry.getValue());
                }
        } else {
            System.out.println("\nNenhuma palavra!");
        }
    }

    public String encontrarPalavraMaisFrequente() {
        String palavraMaisFrequente = null;
        int maiorContagem = Integer.MIN_VALUE;

        if(!this.palavras.isEmpty()) {
            
            for (Map.Entry<String, Integer> entry : palavras.entrySet()) {
                if (entry.getValue() > maiorContagem) {

                    maiorContagem = entry.getValue();
                    palavraMaisFrequente = entry.getKey();
                }
            }
        } else {
            System.out.println("\nNenhuma palavra!");
        }
        return palavraMaisFrequente;
    }
}
