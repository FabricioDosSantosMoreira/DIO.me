package List.Exercicios.Pesquisa.CatalogoDeLivros;


public class Livro {

    // Atributos da classe 'Livro'
    private String titulo;
	private String autor;
	private int anoPublicacao;

    // Construtor da classe 'Livro'
	public Livro(String titulo, String autor, int anoPublicacao) {
		this.titulo = titulo;
		this.autor = autor;
		this.anoPublicacao = anoPublicacao;
	}

	// Método da classe 'Livro'
	@Override
	public String toString() {
		return "Livro [titulo=" + titulo + ", autor=" + autor + ", anoPublicacao=" + anoPublicacao + "]";
	}
	
    // Getters e Setters da classe 'Livro'
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
