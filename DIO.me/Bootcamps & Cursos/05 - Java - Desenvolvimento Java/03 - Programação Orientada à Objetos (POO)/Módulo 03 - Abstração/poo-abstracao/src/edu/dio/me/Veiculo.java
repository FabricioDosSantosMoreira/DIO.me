package edu.dio.me;

abstract class Veiculo {
    
    // Atributo da classe abstrata 'Veiculo'
    public String placa = "";

    // Método construtor da classe abstrata 'Veiculo'
    public Veiculo(String placa) {
        this.placa = placa;
    }

    // Método abstrato que deve ser implementado pelas subclasses
    public abstract void ligar();

    // Método concreto que pode ser acessado pelas subclasses
    protected void verificarCombustivel() {
        System.out.println("Combustível OK!");
    }

    // Método 'getter' e 'setter' da classe abstrata 'Veiculo'
    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }
}
