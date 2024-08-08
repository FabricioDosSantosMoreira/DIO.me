package edu.dio.me.exercicios.map.Pesquisa.EstoqueProdutos;

import java.util.HashMap;
import java.util.Map;

public class EstoqueProduto {

    // Atributo da classe 'EstoqueProduto'
    private Map<Long, Produto> estoqueProdutos;

    // Método construtor da classe 'EstoqueProduto'
    public EstoqueProduto() {
        this.estoqueProdutos = new HashMap<>();
    }

    // Métodos da classe 'EstoqueProduto'
    public void adicionarProduto(long codigo, String nome, double preco,int quantidade) {
        this.estoqueProdutos.put(codigo, new Produto(nome, quantidade, preco));
    }

    public void exibirProdutos() {
        System.out.println(this.estoqueProdutos);
    }

    public Double calcularValorTotalEstoque() {
        Double valorTotalEstoque = 0d;

        if(!this.estoqueProdutos.isEmpty()) {
            for(Produto p : this.estoqueProdutos.values()) {
                valorTotalEstoque += p.getPreco() * p.getQuantidade();
            }
        } else {
            System.out.println("\nO estoque de produtos está vazio!");
        }
        return valorTotalEstoque;
    }

    public Produto obterProdutoMaisCaro() {
        Produto produtoMaisCaro = null;
        double maiorValor = Double.MIN_VALUE;

        if(!this.estoqueProdutos.isEmpty()) {
            for(Produto p : this.estoqueProdutos.values()) {
                if(p.getPreco() > maiorValor) {
                    produtoMaisCaro = p;
                    maiorValor = p.getPreco();
                }
            }
        } else {
            System.out.println("\nO estoque de produtos está vazio!");
        }
        return produtoMaisCaro;
    }

    public Produto obterProdutoMaisBarato() {
        Produto produtoMaisBarato = null;
        double menorValor = Double.MAX_VALUE;

        if(!this.estoqueProdutos.isEmpty()) {
            for(Produto p : this.estoqueProdutos.values()) {
                if(p.getPreco() < menorValor) {
                    produtoMaisBarato = p;
                    menorValor = p.getPreco();
                }
            }
        } else {
            System.out.println("\nO estoque de produtos está vazio!");
        }
        return produtoMaisBarato;
    }

    public Produto obterProdutoMaiorQuantidadeValorTotalNoEstoque() {
        Produto produtoMaiorQuantidadeValorNoEstoque = null;
        double maiorValorTotalProdutoEstoque = 0d;

        if(!this.estoqueProdutos.isEmpty()) {
            for (Map.Entry<Long, Produto> entry : this.estoqueProdutos.entrySet()) {
                double valorProdutoEmEstoque = entry.getValue().getPreco() * entry.getValue().getQuantidade();
                
                if (valorProdutoEmEstoque > maiorValorTotalProdutoEstoque) {
                  maiorValorTotalProdutoEstoque = valorProdutoEmEstoque;
                  produtoMaiorQuantidadeValorNoEstoque = entry.getValue();
                }
            }
        } else {
            System.out.println("\nO estoque de produtos está vazio!");
        }
        return produtoMaiorQuantidadeValorNoEstoque;
    }
}
