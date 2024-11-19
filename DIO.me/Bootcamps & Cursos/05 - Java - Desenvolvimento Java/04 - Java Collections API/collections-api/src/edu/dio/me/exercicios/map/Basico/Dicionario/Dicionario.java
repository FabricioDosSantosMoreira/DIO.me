package edu.dio.me.exercicios.map.Basico.Dicionario;

import java.util.HashMap;
import java.util.Map;

public class Dicionario {

    // Atributos da classe 'Dicionario'
    private Map<String, String> dicionario;

    // Método construtor da classe 'Dicionario'
    public Dicionario() {
        this.dicionario = new HashMap<>();
    }

    // Métodos da classe 'Dicionario'
    public void adicionarPalavra(String palavra, String definicao) {
        this.dicionario.put(palavra, definicao);
    }

    public void removerPalavra(String palavra) {
        if(!this.dicionario.isEmpty()) {
            this.dicionario.remove(palavra);
        } else {
            System.out.println("\nO dicionário está vazio!");
        }
    }

    public void exibirPalavras() {
        System.out.println("\n");
        for (Map.Entry<String, String> entry : this.dicionario.entrySet()) {
			String palavra = entry.getKey();
			String definicao = entry.getValue();

			System.out.println("| palavra: " + palavra + ", definição: " + definicao);
		}
    }

    public String pesquisarPorPalavra(String palavra) {
        String definicao = null;

        if(!this.dicionario.isEmpty()) {
            definicao = this.dicionario.get(palavra);
        } else {
            System.out.println("\nA agenda de contatos está vazia!");
        }
        return definicao;
    }
}
