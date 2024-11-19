package edu.dio.me.comparable;

public class Livro implements Comparable<Livro>{

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

    // Método do Comparable para ordenar livros por título
    @Override
	public int compareTo(Livro l) {
		return titulo.compareTo(l.titulo);
	}
    
    // Método do Comparable para ordenar livros por autor
    // @Override
	// public int compareTo(Livro l) {
	//     return autor.compareTo(l.autor);
	// }

    // Método do Comparable para ordenar livros por ano
    // @Override
	// public int compareTo(Livro l) {
	// 	return ano.compareTo(l.ano);
	// }

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
