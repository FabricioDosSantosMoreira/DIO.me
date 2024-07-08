// │
// │
// │
// └───┬───> Comparable
//     │
//     ├───> O Comparable é uma interface em Java que é usada para definir uma ordem natural de objetos de uma classe. 
//     │       Quando uma classe implementa a interface Comparable, ela precisa fornecer a implementação do método compareTo(), 
//     │        que compara o objeto atual com outro objeto do mesmo tipo.
//     │

//Comparable fornece uma única sequência de ordenação. Em outras palavras, podemos ordenar a coleção com base em um único elemento, como id, nome e preço.
// Comparable afeta a classe original, ou seja, a classe atual é modificada.
// Comparable fornece o método compareTo() para ordenar elementos.
// Comparable está presente no pacote java.lang.
// Podemos ordenar os elementos da lista do tipo Comparable usando o método Collections.sort(List).



package Comparable;

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
        Collections.sort(livros);

        System.out.println("\n+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+");
        for (Livro livro : livros) {
            System.out.println(
                "| Título: " + livro.getTitulo() +
                ", Autor: " + livro.getAutor() +
                ", Ano: " + livro.getAno());
        }
        System.out.println("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+\n");
    }
}
