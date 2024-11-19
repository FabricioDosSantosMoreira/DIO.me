package edu.dio.me;

public class Moto extends Veiculo {

    // Método construtor da classe 'Moto'
    public Moto(String placa) {
        super(placa);
    }

    // OBS: É necessário implementar os métodos de uma classe abstrata
    @Override
    public void ligar() {
        verificarCombustivel();
        System.out.println("Moto ligada!");
    }
}
