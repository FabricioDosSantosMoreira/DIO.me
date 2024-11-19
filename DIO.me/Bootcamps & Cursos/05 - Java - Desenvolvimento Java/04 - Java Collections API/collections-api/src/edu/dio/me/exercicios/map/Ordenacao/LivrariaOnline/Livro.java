package edu.dio.me.exercicios.map.Ordenacao.LivrariaOnline;

import java.util.Comparator;
import java.util.Map;
import java.util.Map.Entry;

public class Livro {

    // Atributos da classe 'Livro'
    private String titulo;
	private String autor;
	private double preco;

    // Método construtor da classe 'Livro'
	public Livro(String titulo, String autor, double preco) {
		this.titulo = titulo;
		this.autor = autor;
		this.preco = preco;
	}

	// Método 'toString()' da classe 'Livro'
	@Override
	public String toString() {
		return "Livro [titulo=" + titulo + ", autor=" + autor + ", preco=" + preco + "]";
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

	public double getPreco() {
		return preco;
	}

	public void setPreco(double preco) {
		this.preco = preco;
	}
}

class ComparatorPorPreco implements Comparator<Map.Entry<String, Livro>> {
	@Override
	public int compare(Entry<String, Livro> l1, Entry<String, Livro> l2) {
		return Double.compare(l1.getValue().getPreco(), l2.getValue().getPreco());
	}
}
