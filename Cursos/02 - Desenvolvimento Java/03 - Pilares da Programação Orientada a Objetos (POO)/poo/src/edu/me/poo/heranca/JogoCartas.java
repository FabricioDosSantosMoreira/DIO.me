package edu.me.poo.heranca;

public class JogoCartas extends Jogo {

    // Atributos
    private int qntdCartas;
    
    // Método construtor completo
    public JogoCartas(String nome, int nrJogadores, int qntdCartas) {
        super(nome, nrJogadores);
        this.qntdCartas = qntdCartas;
    }

    // Métodos getters
    public int getQntdCartas() {
        return qntdCartas;
    }

    // Métodos setters
    public void setQntdCartas(int qntdCartas) {
        this.qntdCartas = qntdCartas;
    }

    // Métodos da classe JogoCartas
    public void comprarCarta() {
        System.out.println("\nCarta comprada!");
    }
    public void descartarCarta() {
        System.out.println("\nCarta descartada!");
    }
    public void jogarCarta() {
        System.out.println("\nCarta jogade!");
    }

    public void infoJogoCartas() {
        super.infoJogo(); //Chama o infoJogo lá da classe mãe (não pode usar @Override)
        System.out.println("\nNome: " + nome +
                            "\nN° Jogadores: " + nrJogadores +
                            "\nQuantidade de cartas: " + qntdCartas);
    }
}