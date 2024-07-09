package SetInterface.Exercicios.Ordenacao.CadastroDeProdutos;

import java.util.Comparator;
import java.util.Objects;


public class Produto implements Comparable<Produto> {

    // Atributos da classe 'Produto'
    private long codigo;
    private String nome;
    private double preco;
    private int quantidade;

    // Construtor da classe 'Produto'
    public Produto(long codigo, String nome, double preco, int quantidade) {
        this.codigo = codigo;
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    // Método 'toString' da classe 'Produto'
    @Override
    public String toString() {
        return "Produto{codigo=" + codigo + ", nome=" + nome + ", preco=" + preco + ", quantidade=" + quantidade + "}";
    }

    // Método 'hashCode' da classe 'Produto'
    @Override
    public int hashCode() {
        return Objects.hash(getCodigo());
    }

    // Método 'equals' da classe 'Produto'
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Produto produto)) return false;
        return getCodigo() == produto.getCodigo();
    }

    // Método 'compareTo' da classe 'Produto'
    @Override
    public int compareTo(Produto p) {
        return this.nome.compareToIgnoreCase(p.getNome());
    }

    // Getters e Setters da classe 'Produto'
    public long getCodigo() {
        return codigo;
    }

    public void setCodigo(long codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }
}

class ComparatorPorPreco implements Comparator<Produto> {
    @Override
    public int compare(Produto p1, Produto p2) {
        return Double.compare(p1.getPreco(), p2.getPreco());
    }
}
