package Comparable;


public class Livro implements Comparable<Livro>{

    // Atributos da classe Livro
    private String titulo;
	private String autor;
	private Integer ano;


    // Construtor da classe Livro
	public Livro(String titulo, String autor, Integer ano) {
		this.titulo = titulo;
		this.autor = autor;
		this.ano = ano;
	}


    // Usado para ordenar livros por título
    @Override
	public int compareTo(Livro l) {
		return titulo.compareTo(l.titulo);
	}
    
    // Usado para ordenar livros por autor
    // @Override
	// public int compareTo(Livro l) {
	//     return autor.compareTo(l.autor);
	// }

    // Usado para ordenar livros por ano
    // @Override
	// public int compareTo(Livro l) {
	//	return ano.compareTo(l.ano);
	//}


    // Getters 
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
