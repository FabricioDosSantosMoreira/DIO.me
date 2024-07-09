package List.Exercicios.Ordenacao.OrdenacaoDePessoas;

public class Pessoa implements Comparable<Pessoa> {

    // Atributos da classe 'Pessoa'
    private String nome;
    private int idade;
    private double altura;

    // Construtor da classe 'Pessoa'
    public Pessoa(String nome, int idade, double altura) {
        this.nome = nome;
        this.idade = idade;
        this.altura = altura;
    }

    // Métodos da classe 'Pessoa'
    @Override
    public int compareTo(Pessoa p) {
        // Compara por idade
        return Integer.compare(this.getIdade(), p.getIdade());
    }

    @Override
    public String toString() {
        return "Pessoa{" + "nome='" + nome + '\'' + ", idade=" + idade +", altura=" + altura +'}';
    }

    // Getters e Setters da classe 'Pessoa'
    public String getNome() {
        return nome;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }
}
