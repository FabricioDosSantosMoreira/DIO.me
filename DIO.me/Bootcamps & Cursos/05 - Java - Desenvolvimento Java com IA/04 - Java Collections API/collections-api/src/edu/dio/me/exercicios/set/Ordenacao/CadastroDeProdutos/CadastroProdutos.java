package edu.dio.me.exercicios.set.Ordenacao.CadastroDeProdutos;

import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class CadastroProdutos {

    // Atributo da classe 'CadastroProdutos'
    private Set<Produto> produtoSet;

    // Construtor da classe 'CadastroProdutos'
    public CadastroProdutos() {
        this.produtoSet = new HashSet<>();
    }

    // Métodos da classe 'CadastroProdutos'
    public void adicionarProduto(long codigo, String nome, double preco, int quantidade) {
        this.produtoSet.add(new Produto(codigo, nome, preco, quantidade));
    }

    public Set<Produto> exibirProdutosPorNome() {
        // Organiza por nome. O TreeSet detecta o método 'compareTo' de 'Produto'
        Set<Produto> produtosPorNome = new TreeSet<>(this.produtoSet);
        return produtosPorNome;
    }

    public Set<Produto> exibirProdutosPorPreco() {
        Set<Produto> produtosPorPreco = new TreeSet<>(new ComparatorPorPreco());
        produtosPorPreco.addAll(this.produtoSet);
        return produtosPorPreco;
    }
}
