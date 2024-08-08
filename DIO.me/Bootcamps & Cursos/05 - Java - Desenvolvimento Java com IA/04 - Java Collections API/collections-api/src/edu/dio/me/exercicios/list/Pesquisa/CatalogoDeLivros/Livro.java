package edu.dio.me.exercicios.list.Pesquisa.CatalogoDeLivros;

public class Livro {

    // Atributos da classe 'Livro'
    private String titulo;
	private String autor;
	private int anoPublicacao;

    // Método construtor da classe 'Livro'
	public Livro(String titulo, String autor, int anoPublicacao) {
		this.titulo = titulo;
		this.autor = autor;
		this.anoPublicacao = anoPublicacao;
	}

	// Método 'toString()' da classe 'Livro'
	@Override
	public String toString() {
		return "Livro [titulo=" + titulo + ", autor=" + autor + ", anoPublicacao=" + anoPublicacao + "]";
	}
	
    // Métodos 'getters' e 'setters' da classe 'Livro'
	public String getTitulo() {
		return titulo;
	}

	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}

	public String getAutor() {
		return autor;
	}

	public void setAutor(String autor) {
		this.autor = autor;
	}

	public int getAnoPublicacao() {
		return anoPublicacao;
	}

	public void setAnoPublicacao(int anoPublicacao) {
		this.anoPublicacao = anoPublicacao;
	}
}
