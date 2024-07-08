package List.Exercicios.Pesquisa.CatalogoDeLivros;

import java.util.ArrayList;
import java.util.List;


public class CatalogoLivros {

    private List<Livro> catalogo;

    public CatalogoLivros() {
        this.catalogo = new ArrayList<>();
    }

    public void adicionarLivro(String titulo, String autor, int anoPublicacao) {
        this.catalogo.add(new Livro(titulo, autor, anoPublicacao));
    }

    public List<Livro> pesquisarPorAutor(String autor) {
        List<Livro> livrosEncontrados = new ArrayList<>();

        if(!this.catalogo.isEmpty()) {
            for (Livro l : this.catalogo) {
                if (l.getAutor().equalsIgnoreCase(autor)) {
                    livrosEncontrados.add(l);
                }
            }
        } else {
            System.out.println("\nO catálogo de livros está vazio!");
        }

        return livrosEncontrados;
    }

    public Livro pesquisarPorTitulo(String titulo) {
        Livro livroEncontrado = null;

        if(!this.catalogo.isEmpty()) {
            for (Livro l : this.catalogo) {
                if (l.getTitulo().equalsIgnoreCase(titulo)) {
                    livroEncontrado = l;
                    break;
                }
            }
        } else {
            System.out.println("\nO catálogo de livros está vazio!");
        }

        return livroEncontrado;
    }
    
    public List<Livro> pesquisarPorIntervaloAnos(int anoInicial, int anoFinal) {
        List<Livro> livrosEncontrados = new ArrayList<>();

        if(!this.catalogo.isEmpty()) {
            for (Livro l : this.catalogo) {
                if (l.getAnoPublicacao() >= anoInicial && l.getAnoPublicacao() <= anoFinal) {
                    livrosEncontrados.add(l);
                }
            }
        } else {
            System.out.println("\nO catálogo de livros está vazio!");
        }

        return livrosEncontrados;
    }
}
