package edu.dio.me.exercicios.set.Basico.ConjuntoDePalavrasUnicas;

import java.util.HashSet;
import java.util.Set;

public class ConjuntoPalavrasUnicas {

    // Atributo da classe 'ConjuntoPalavrasUnicas'
    private Set<String> palavras;

    // Construtor da classe 'ConjuntoPalavrasUnicas'
    public ConjuntoPalavrasUnicas() {
        this.palavras = new HashSet<>();
    }

    // Métodos da classe 'ConjuntoPalavrasUnicas'
    public void adicionarPalavra(String palavra) {
        this.palavras.add(palavra);
    }

    public void removerPalavra(String palavra) {
        this.palavras.remove(palavra);
    }

    public void verificarPalavra(String palavra) {
 
        if(!this.palavras.isEmpty()) {

            if (this.palavras.contains(palavra)) {
                    System.out.println("\nEssa palavra existe!");
            } else {
                System.out.println("\nEssa palavra não existe!");
            }
        } else {
            System.out.println("\nNenhuma palavra!");
        }
    }

    public void exibirPalavrasUnicas() {
        if(!this.palavras.isEmpty()) {
            for(String p : this.palavras) {
                System.out.println("| Palavra: " + p);              
            }
        } else {
            System.out.println("\nNenhuma palavra!");
        }
    }
}
