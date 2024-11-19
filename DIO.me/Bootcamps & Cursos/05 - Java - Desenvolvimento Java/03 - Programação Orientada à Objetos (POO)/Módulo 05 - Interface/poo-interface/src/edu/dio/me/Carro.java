package edu.dio.me;

interface Veiculo {

    default void ligar() {
        System.out.println("O veículo está ligado.");
    }
    
    static void abastecer() {
        System.out.println("O veículo está abastecendo.");
    }
}


interface Navegador {

    void navegar();
}


public class Carro implements Veiculo, Navegador{

    @Override
    public void navegar() {
        System.out.println("Navegando...");
    }
}   
