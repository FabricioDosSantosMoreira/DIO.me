package Map.Exercicios.Pesquisa.EstoqueProdutos;

public class Produto {
    
    // Atributos da classe 'Produto'
    private String nome;
    private int quantidade;
    private double preco;

    // Construtor da classe 'Produto'
    public Produto(String nome, int quantidade, double preco) {
        this.nome = nome;
        this.quantidade = quantidade;
        this.preco = preco;
    }

    // Método 'toString' da classe 'Produto'
    @Override
    public String toString() {
        return "Produto [nome=" + nome + ", quantidade=" + quantidade + ", preco=" + preco + "]";
    }

    // Getters e Setters da classe 'Produto'
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }
}
