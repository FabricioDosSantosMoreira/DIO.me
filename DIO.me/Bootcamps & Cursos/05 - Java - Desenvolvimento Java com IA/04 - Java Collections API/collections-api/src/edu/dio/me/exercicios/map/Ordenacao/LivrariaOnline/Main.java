// ├───────> Exercício - Livraria Online:
// │             Crie uma classe chamada 'LivrariaOnline' que representa uma livraria online. Essa 
// │         classe utiliza um Map para armazenar os livros disponíveis na livraria, utilizando o 
// │         link da obra na Amazon Marketplace como chave e um objeto da classe 'Livro' como 
// │         valor. A classe 'Livro' possui atributos como título, autor e preço. Através da 
// │         classe 'LivrariaOnline', implemente os seguintes métodos:
// │
// │             * adicionarLivro(String link, String titulo, String autor, double preco):
// │                   Adiciona um livro à livraria, utilizando o ISBN como chave no Map.
// │
// │             * removerLivro(String titulo): 
// │                   Remove um livro da livraria, dado o titulo do livro.
// │
// │             * exibirLivrosOrdenadosPorPreco():
// │                   Exibe os livros da livraria em ordem crescente de preço.
// │
// │             * pesquisarLivrosPorAutor(String autor):
// │                   Retorna uma lista de todos os livros escritos por um determinado autor.
// │
// │             * obterLivroMaisCaro():
// │                   Retorna o livro mais caro disponível na livraria.
// │
// │             * obterLivroMaisBarato():
// │                   Retorna o livro mais barato disponível na livraria.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.map.Ordenacao.LivrariaOnline;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        
        // Instânciando um objeto da classe 'CatalogoLivros'
        LivrariaOnline livaria = new LivrariaOnline();

        // Adicionando livros
        livaria.adicionarLivro("123", "Admirável Mundo Novo", "Aldous Huxley", 50);
        livaria.adicionarLivro("1234", "Periféricos", "William Gibson", 50);
        livaria.adicionarLivro("12345", "O Guia do Mochileiro das Galáxias", "Douglas Adams", 100);
        livaria.adicionarLivro("123456", "Cosmos", "Carl Sagan", 80);
        livaria.adicionarLivro("1234567", "O Mundo Assombrado pelos Demônios", "Carl Sagan", 67);
        
        livaria.removerLivro("Admirável Mundo Novo");

        livaria.exibirLivrosOrdenadosPorPreco();

        // Pesquisando livros por autor
        System.out.println("\nPesquisa por autor: ");
        List<Livro> livros = livaria.pesquisarLivrosPorAutor("Carl Sagan");
        System.out.println(livros);

        Livro livroMaisCaro = livaria.obterLivroMaisCaro();
        System.out.println("Livro mais caro: " + livroMaisCaro);

        Livro livroMaisbarato = livaria.obterLivroMaisBarato();
        System.out.println("Livro mais caro: " + livroMaisbarato);
    }
}
