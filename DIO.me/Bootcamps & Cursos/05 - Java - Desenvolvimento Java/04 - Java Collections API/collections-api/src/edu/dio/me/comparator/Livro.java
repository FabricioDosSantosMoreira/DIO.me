package edu.dio.me.comparator;

import java.util.Comparator;

public class Livro {

    // Atributos da classe 'Livro'
    private String titulo;
	private String autor;
	private Integer ano;


    // Método construtor da classe 'Livro'
	public Livro(String titulo, String autor, Integer ano) {
		this.titulo = titulo;
		this.autor = autor;
		this.ano = ano;
	}

    // Métodos 'getter' da classe 'Livro'
	public String getTitulo() {
		return titulo;
	}

	public String getAutor() {
		return autor;
	}

	public int getAno() {
		return ano;
	}
}


// Classe para comparar Livro por título
class CompararTitulo implements Comparator<Livro> {
    @Override
    public int compare(Livro l1, Livro l2) {
        return l1.getTitulo().compareTo(l2.getTitulo());
    }
}


// Classe do Comparator para comparar livros por autor
class CompararAutor implements Comparator<Livro> {
    @Override
    public int compare(Livro l1, Livro l2) {
        return l1.getAutor().compareTo(l2.getAutor());
    }
}
  

// Classe do Comparator para comparar livros por ano
class CompararAno implements Comparator<Livro> {
    @Override
    public int compare(Livro l1, Livro l2) {
        return Integer.compare(l1.getAno(), l2.getAno());
    }
}


// Classe do Comparator para comparar livros por ano, autor e título
class CompararAnoAutorTitulo implements Comparator<Livro> {
    @Override
    public int compare(Livro l1, Livro l2) {
        int ano = Integer.compare(l1.getAno(), l2.getAno());
        if (ano != 0)
            return ano;

        int autor = l1.getAutor().compareTo(l2.getAutor());
        if (autor != 0)
            return autor;
            
        return l1.getTitulo().compareTo(l2.getTitulo());
    }
}
