// ├───────> Exercício - Catálogo de Livros:
// │             Crie uma classe chamada 'CatalogoLivros' que possui uma lista de objetos do 
// │         tipo 'Livro' como atributo. Cada livro possui atributos como título, autor e 
// │         ano de publicação. Implemente os seguintes métodos:
// │
// │            * adicionarLivro(String titulo, String autor, int anoPublicacao): 
// │                  Adiciona um livro ao catálogo.
// │ 
// │            * pesquisarPorAutor(String autor): 
// │                  Pesquisa livros por autor e retorna uma lista com os livros encontrados.
// │ 
// │            * pesquisarPorTitulo(String titulo): 
// │                  Pesquisa livros por título e retorna o primeiro livro encontrado.
// │ 
// │            * pesquisarPorIntervaloAnos(int anoInicial, int anoFinal): 
// │                  Pesquisa livros publicados em um determinado intervalo de anos e retorna uma 
// │                  lista com os livros encontrados.
// │ 
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.list.Pesquisa.CatalogoDeLivros;

import java.util.List;

public class Main {
    
    public static void main(String[] args) {

        // Instânciando um objeto da classe 'CatalogoLivros'
        CatalogoLivros catalogo = new CatalogoLivros();

        // Adicionando livros
        catalogo.adicionarLivro("Admirável Mundo Novo", "Aldous Huxley", 1932);
        catalogo.adicionarLivro("Periféricos", "William Gibson", 2014);
        catalogo.adicionarLivro("O Guia do Mochileiro das Galáxias", "Douglas Adams", 1979);
        catalogo.adicionarLivro("Cosmos", "Carl Sagan", 1980);
        catalogo.adicionarLivro("O Mundo Assombrado pelos Demônios", "Carl Sagan", 1995);
        
        // Pesquisando livros por autor
        System.out.println("\nPesquisa por autor: ");
        List<Livro> livros = catalogo.pesquisarPorAutor("Carl Sagan");
        System.out.println(livros);

        // Pesquisando livros por título
        System.out.println("\nPesquisa por título:");
        Livro livro = catalogo.pesquisarPorTitulo("Periféricos");
        System.out.println(livro);

        // Pesquisando livros por interavalo de anos
        System.out.println("\nPesquisa por intervalo de anos: ");
        livros = catalogo.pesquisarPorIntervaloAnos(1980, 2020);
        System.out.println(livros);
    }
}
