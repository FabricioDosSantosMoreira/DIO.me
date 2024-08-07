// ├───────> Exercício - Carrinho de Compras:
// │             Crie uma classe chamada 'CarrinhoDeCompras' que representa um carrinho de  
// │         compras. O carrinho deve ser implementado como uma lista de itens. Cada item
// │         é representado por uma classe chamada 'Item' que possui atributos como nome, 
// │         preço e quantidade. Implemente os seguintes métodos:
// │
// │            * adicionarItem(String nome, double preco, int quantidade): 
// │                  Adiciona um item ao carrinho com o nome, preço e quantidade especificados.
// │ 
// │            * removerItem(String nome): 
// │                  Remove um item do carrinho com base no seu nome.
// │ 
// │            * calcularValorTotal(): 
// │                  Calcula e retorna o valor total do carrinho, levando em consideração o preço e a 
// │                  quantidade de cada item.
// │ 
// │            * exibirItens(): 
// │                  Exibe todos os itens presentes no carrinho, mostrando seus nomes, preços e quantidades.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.list.Basico.CarrinhoDeCompras;

public class Main {
    
    public static void main(String[] args) {

        // Instânciando um objeto da classe 'CarrinhoDeCompras'
        CarrinhoDeCompras carrinhoDeCompras = new CarrinhoDeCompras();

        // Adicionando itens
        carrinhoDeCompras.adicionarItem("item 1", 10.0, 10);
        carrinhoDeCompras.adicionarItem("item 2", 20.0, 20);
        carrinhoDeCompras.adicionarItem("item 3", 30.0, 30);

        // Exibindo o valor total de itens
        System.out.println("\nO valor dos itens é: " + carrinhoDeCompras.calcularValorTotal());

        // Exibindo os itens
        carrinhoDeCompras.exibirItens();

        // Removendo um item
        carrinhoDeCompras.removerItem("Item 1");

        // Exibindo o valor total de itens
        System.out.println("\nO valor dos itens é: " + carrinhoDeCompras.calcularValorTotal());

        // Exibindo os itens
        carrinhoDeCompras.exibirItens();

        // Removendo itens
        carrinhoDeCompras.removerItem("Item 2");
        carrinhoDeCompras.removerItem("Item 3");

        // Exibindo o valor total de itens
        System.out.println("\nO valor dos itens é: " + carrinhoDeCompras.calcularValorTotal());

        // Exibindo os itens
        carrinhoDeCompras.exibirItens();
    }
}
