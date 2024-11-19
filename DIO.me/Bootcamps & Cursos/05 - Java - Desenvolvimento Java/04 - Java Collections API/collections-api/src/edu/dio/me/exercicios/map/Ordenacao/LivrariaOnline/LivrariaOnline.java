package edu.dio.me.exercicios.map.Ordenacao.LivrariaOnline;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LivrariaOnline {

    // Atributo da classe 'LivrariaOnline'
    private Map<String, Livro> livraria;

    // Método construtor da classe 'LivrariaOnline'
    public LivrariaOnline() {
        this.livraria = new HashMap<>();
    }

    // Métodos da classe 'LivrariaOnline'
    public void adicionarLivro(String link, String titulo, String autor, double preco) {
        this.livraria.put(link, new Livro(titulo, autor, preco));
    }

    public void removerLivro(String titulo) {
        Livro livroParaRemover = null;

        if(!this.livraria.isEmpty()) {
            for (Map.Entry<String, Livro> entry : this.livraria.entrySet()) {

                livroParaRemover = entry.getValue();
                String link = entry.getKey();
                if (livroParaRemover.getTitulo().equals(titulo)) {
                    this.livraria.remove(link);
                    break;
                }
            }
        } else {
            System.out.println("\nA livraria está vazia!");
        }
    }

    public void exibirLivrosOrdenadosPorPreco() {
        List<Map.Entry<String, Livro>> livrosParaOrdenar = new ArrayList<>(livraria.entrySet());

        Collections.sort(livrosParaOrdenar, new ComparatorPorPreco());

        for (Map.Entry<String, Livro> entry : livrosParaOrdenar) {
            System.out.println("| Livro: " + entry.getValue());
        }
    }
       
    public List<Livro> pesquisarLivrosPorAutor(String autor) {
        List<Livro> livrosDoAutor = new ArrayList<>();

        if(!this.livraria.isEmpty()) {
            for (Map.Entry<String, Livro> entry : this.livraria.entrySet()) {
                if (entry.getValue().getAutor().equals(autor)) {
                    livrosDoAutor.add(entry.getValue());
                }
            }
        } else {
            System.out.println("\nA livraria está vazia!");
        }
        return livrosDoAutor;
    }

    public Livro obterLivroMaisCaro() {
        Livro livro = null;
        double valorMaisCaro = Double.MIN_VALUE;

        if(!this.livraria.isEmpty()) {
            for (Map.Entry<String, Livro> entry : this.livraria.entrySet()) {
                if (entry.getValue().getPreco() > valorMaisCaro) {
                    valorMaisCaro = entry.getValue().getPreco();
                    livro = entry.getValue();
                }
            }
        } else {
            System.out.println("\nA livraria está vazia!");
        }
        return livro;
    }

    public Livro obterLivroMaisBarato() {
        Livro livro = null;
        double valorMaisBarato = Double.MAX_VALUE;

        if(!this.livraria.isEmpty()) {
            for (Map.Entry<String, Livro> entry : this.livraria.entrySet()) {
                if (entry.getValue().getPreco() < valorMaisBarato) {
                    valorMaisBarato = entry.getValue().getPreco();
                    livro = entry.getValue();
                }
            }
        } else {
            System.out.println("\nA livraria está vazia!");
        }
        return livro;
    }
}
