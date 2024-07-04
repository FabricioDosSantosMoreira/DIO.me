package edu.me.poo.heranca;

public class JogoTabuleiro extends Jogo {

	// Atributos
    private int qntdPecas;

    // Método construtor completo
	public JogoTabuleiro(String nome, int nrJogadores, int qntdPecas) {
		super(nome, nrJogadores);
		this.qntdPecas = qntdPecas;
    }	
    
    // Métodos getters
	public int getQntdPecas() {
		return qntdPecas;
	}
	
	// Métodos setters
	public void setQntdPecas(int qntdPecas) {
		this.qntdPecas = qntdPecas;
	}
    
	// Métodos da classe JogoTabuleiro
	public void setupTabuleiro() {
		System.out.println("\nTabuleiro montado!");
	}
    
	public void moverPeca() {
		System.out.println("\nPeça movida!");
	}

    @Override // Sobreescreve o método infoJogo da classe mãe
    public void infoJogo() {
        System.out.println("\nNome: " + nome +
                            "\nN° Jogadores: " + nrJogadores +
                            "\nQuantidade de peças: " + qntdPecas);
   } 
}