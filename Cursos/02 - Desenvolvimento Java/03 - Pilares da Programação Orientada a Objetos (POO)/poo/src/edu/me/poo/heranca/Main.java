package edu.me.poo.heranca;

public class Main {
    public static void main(String[] args) {
        
        JogoTabuleiro xadrez = new JogoTabuleiro(null, 0, 0);
        // Atributos da classe JogoTabuleiro (classe mãe)
        xadrez.setQntdPecas(32);
        // Atributos através da herança (classe filha)
        xadrez.setNome("Xadrez");
        xadrez.setNrJogadores(2);
        // Métodos da classe mãe
        xadrez.jogar();
        // Métodos da classe filha
        xadrez.setupTabuleiro();
        xadrez.moverPeca();

        JogoTabuleiro damas =new JogoTabuleiro("Damas", 2, 12);
        

        JogoCartas baralho = new JogoCartas("Baralho", 4, 52);
        baralho.comprarCarta();
        baralho.descartarCarta();
        baralho.infoJogoCartas();
    }    
}
