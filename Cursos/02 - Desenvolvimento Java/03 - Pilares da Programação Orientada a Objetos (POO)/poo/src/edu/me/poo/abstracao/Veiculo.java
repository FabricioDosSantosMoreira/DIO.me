package edu.me.poo.abstracao;


/*
Em Java, abstração é um conceito de programação orientada a objetos (POO) 
que se refere à capacidade de se focar nos aspectos essenciais de um objeto, 
ignorando os detalhes não essenciais. A abstração permite que os desenvolvedores 
criem classes e objetos que representam conceitos genéricos, encapsulando detalhes 
específicos de implementação e fornecendo uma interface clara para a interação com esses objetos.
*/

abstract class Veiculo {

    public String placa = "";

    public Veiculo(String placa) {
        this.placa = placa;
    }

    // Método abstrato (não tem corpo)
    public abstract void ligar();

    // Método concreto
    public void verificarCombustivel() {
        System.out.println("\nCombustível OK!");
    }

    // Getters e Setters
    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }
}

class Carro extends Veiculo {

    public Carro(String placa) {
        super(placa);
    }

    @Override
    public void ligar() {
        verificarCombustivel();
        System.out.println("\nCarro ligado!");
    }
}

class Moto extends Veiculo {

    public Moto(String placa) {
        super(placa);
    }

    @Override
    public void ligar() {
        verificarCombustivel();
        System.out.println("\nMoto ligada!");
    }
}