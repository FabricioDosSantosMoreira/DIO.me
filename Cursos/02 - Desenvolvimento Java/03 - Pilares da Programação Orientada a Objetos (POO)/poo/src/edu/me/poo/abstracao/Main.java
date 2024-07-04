package edu.me.poo.abstracao;

public class Main {
    public static void main(String[] args) {
        Veiculo carro = new Carro("ABC-1234");
        Veiculo moto = new Moto("ABC-1234");

        carro.ligar();
        moto.ligar();
    }

}
