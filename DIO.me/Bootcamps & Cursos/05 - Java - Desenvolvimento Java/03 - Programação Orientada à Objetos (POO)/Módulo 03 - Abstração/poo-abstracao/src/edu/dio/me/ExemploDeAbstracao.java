package edu.dio.me;

public class ExemploDeAbstracao {
    
    // - - - - - > Abstração:
    //                 A abstração é dos princípios fundamentais da programação orientada a objetos (POO) 
    //             em Java. Ela se refere à capacidade de se focar nos aspectos essenciais de um objeto, 
    //             ignorando os detalhes não essenciais. A abstração permite que os desenvolvedores 
    //             criem classes e objetos que representam conceitos genéricos, encapsulando 
    //             detalhes específicos de implementação e fornecendo uma interface clara 
    //             para a interação com esses objetos.

    public static void main(String[] args) {
        
        // Criando objetos da classe 'Moto'
        Moto moto = new Moto("ABC-1234");
        
        // Usando os métodos da classe 'Moto'
        moto.ligar();
        moto.verificarCombustivel();
    }
}
