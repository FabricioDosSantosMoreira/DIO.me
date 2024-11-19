package edu.dio.me.exercicios.list.Basico.CarrinhoDeCompras;

import java.util.ArrayList;
import java.util.List;

public class CarrinhoDeCompras {

    // Atributo da classe 'CarrinhoDeCompras'
    private List<Item> listaItens;

    // Método construtor da classe 'CarrinhoDeCompras'
    public CarrinhoDeCompras() {
        this.listaItens = new ArrayList<>();
    }

    // Métodos da classe 'CarrinhoDeCompras'
    public void adicionarItem(String nome, double preco, int quantidade) {
        this.listaItens.add(new Item(nome, preco, quantidade));
    }

    public void removerItem(String nome) {
        if (!this.listaItens.isEmpty()) {
            List<Item> itensParaRemover = new ArrayList<>();

            for (Item i : this.listaItens) {
                if (i.getNome().equalsIgnoreCase(nome)) {
                    itensParaRemover.add(i);
                }
            }

            this.listaItens.removeAll(itensParaRemover);
        } else {
            System.out.println("\nA lista está vazia!");
        }
    }

    public double calcularValorTotal() {
        double valorTotal = 0.0;
        
        for (Item i : this.listaItens) {
            valorTotal += i.getPreco() * i.getQuantidade();
        } 
        return valorTotal;
    }

    public void exibirItens() {
        if (!this.listaItens.isEmpty()) {
            
            System.out.println("\n| Lista de itens: ");
            for (Item i : this.listaItens) {
                System.out.println(
                    "| Nome: " + i.getNome() +
                    ", Preço " + i.getPreco() +
                    ", Quantidade " + i.getQuantidade()
                );
            }
        } else {
            System.out.println("\nA lista está vazia!");
        }
    }
}
