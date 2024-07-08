// Em Java, um Comparator é uma interface funcional que permite definir uma ordem de classificação personalizada para objetos de uma classe. Geralmente é usada em conjunto com coleções como List, Set, e Map, que oferecem métodos de ordenação que aceitam um Comparator como argumento.

// Um Comparator define um método compare() que compara dois objetos e retorna um valor inteiro que indica a relação de ordem entre eles:

// Retorna um valor negativo se o primeiro objeto é considerado menor que o segundo.
// Retorna zero se os objetos são considerados iguais.
// Retorna um valor positivo se o primeiro objeto é considerado maior que o segundo.
// Isso permite que você ordene objetos com base em critérios personalizados que não são a ordem natural definida pela classe dos objetos. Por exemplo, você pode usar um Comparator para ordenar uma lista de objetos Pessoa por idade, nome, ou qualquer outro critério que deseje aplicar.




// O Comparator fornece o método compare() para ordenar elementos.
// O Comparator fornece múltiplas sequências de ordenação. Em outras palavras, podemos ordenar a coleção com base em múltiplos elementos, como id, nome, preço, etc.
// O Comparator não afeta a classe original, ou seja, a classe atual não é modificada.
// Um Comparator está presente no pacote java.util.
// Podemos ordenar os elementos da lista do tipo Comparator usando o método Collections.sort(List, Comparator).

package Comparator;

import java.util.ArrayList;
import java.util.Collections;


public class Main {
    public static void main(String[] args) {
        // Criação da lista de livros
        ArrayList<Livro> livros = new ArrayList<>();      

        
        // Adicionando livros à lista
        livros.add(new Livro("Admirável Mundo Novo", "Aldous Huxley", 1932));
        livros.add(new Livro("Periféricos", "William Gibson", 2014));
        livros.add(new Livro("O Guia do Mochileiro das Galáxias", "Douglas Adams", 1979));
        livros.add(new Livro("Morte Feliz", "Albert Camus", 1971));
        livros.add(new Livro("Cosmos", "Carl Sagan", 1980));
        

        // Ordenando a lista de livros pelo título
        Collections.sort(livros, new CompararTitulo());
        
        System.out.println("\n+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+");
        System.out.println("| Livros após a ordenação por título: ");
        for (Livro livro : livros) {
            System.out.println(
                "| Título: " + livro.getTitulo() +
                ", Autor: " + livro.getAutor() +
                ", Ano: " + livro.getAno());
        }
        System.out.println("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+\n");
    
        
        // Ordenando a lista de livros pelo autor
        Collections.sort(livros, new CompararAutor());
        
        System.out.println("\n+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+");
        System.out.println("| Livros após a ordenação por autor: ");
        for (Livro livro : livros) {
            System.out.println(
                "| Título: " + livro.getTitulo() +
                ", Autor: " + livro.getAutor() +
                ", Ano: " + livro.getAno());
        }
        System.out.println("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+\n");
        

        // Ordenando a lista de livros pelo ano
        Collections.sort(livros, new CompararAno());
        
        System.out.println("\n+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+");
        System.out.println("| Livros após a ordenação por ano: ");
        for (Livro livro : livros) {
            System.out.println(
                "| Título: " + livro.getTitulo() +
                ", Autor: " + livro.getAutor() +
                ", Ano: " + livro.getAno());
        }
        System.out.println("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+\n");


        // Ordenando a lista de livros pelo ano, autor e título 
        Collections.sort(livros, new CompararAnoAutorTitulo());

        System.out.println("\n+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+");
        System.out.println("| Livros após a ordenação por ano, autor e título: ");
        for (Livro livro : livros) {
            System.out.println(
                "| Título: " + livro.getTitulo() +
                ", Autor: " + livro.getAutor() +
                ", Ano: " + livro.getAno());
        }
        System.out.println("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+\n");
    }
}
