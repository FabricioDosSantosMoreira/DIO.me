package List.Exercicios.Basico.CarrinhoDeCompras;

import java.util.ArrayList;
import java.util.List;


public class CarrinhoDeCompras {

    private List<Item> itens;

    public CarrinhoDeCompras() {
        this.itens = new ArrayList<>();
    }

    public void adicionarItem(String nome, double preco, int quantidade) {
        this.itens.add(new Item(nome, preco, quantidade));
    }

    public void removerItem(String nome) {
        if (!this.itens.isEmpty()) {
            List<Item> itensParaRemover = new ArrayList<>();

            for (Item i : this.itens) {
                if (i.getNome().equalsIgnoreCase(nome)) {
                    itensParaRemover.add(i);
                }
            }

            this.itens.removeAll(itensParaRemover);

        } else {
            System.out.println("\nA lista está vazia!");
        }
    }

    public double calcularValorTotal() {
        double valorTotal = 0.0;
        
        for (Item i : this.itens) {
            valorTotal += i.getPreco() * i.getQuantidade();
        } 

        return valorTotal;
    }

    public void exibirItens() {
        if (!this.itens.isEmpty()) {
            System.out.println("\n| Lista de itens: ");
            for (Item i : this.itens) {
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
