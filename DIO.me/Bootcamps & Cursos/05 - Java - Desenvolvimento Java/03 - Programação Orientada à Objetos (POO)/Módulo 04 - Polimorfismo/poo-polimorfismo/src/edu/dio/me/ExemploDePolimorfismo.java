package edu.dio.me;

public class ExemploDePolimorfismo {

    // - - - - - > Polimorfismo:
    //                 O polimorfismo é dos princípios fundamentais da programação orientada a objetos (POO) 
    //             em Java. Ele se refere à capacidade de um objeto se comportar de diferentes maneiras 
    //             dependendo de seu tipo de referência ou do contexto. Ele se manifesta principalmente 
    //             de duas formas: sobrecarga (overload) e sobrescrita(override), existe também o 
    //             polimorfismo de subtipo.
    //
    // - - - - > Tipos de Polimorfismo:
    //
    // - - - > Polimorfismo de Sobrecarga:
    //             Polimorfismo de sobrecarga é quando duas ou mais funções na mesma classe têm o mesmo nome, 
    //         mas diferentes parâmetros. Isso permite que você use o mesmo nome de método para realizar 
    //         operações semelhantes, mas com diferentes tipos ou números de argumentos.
    //
    // - - - > Polimorfismo de Sobrescrita:
    //             Polimorfismo de sobrescrita é quando uma subclasse fornece uma implementação específica 
    //         para um método que já está definido em sua superclasse. A assinatura do método na 
    //         subclasse deve ser a mesma que na superclasse. Isso permite que o comportamento 
    //         do método seja modificado de acordo com a subclasse.
    //
    // - - - > Polimorfismo de Subtipo:
    //             Polimorfismo de subtipo é quando um objeto de uma subclasse é tratado como objeto da 
    //         superclasse. Isso é útil para escrever código que pode trabalhar com diferentes 
    //         tipos de objetos de forma genérica.

    public static void main(String[] args) {
        
        // Uso do polimorfismo de sobrecarga
        Calculadora calculadora = new Calculadora();

        System.out.println(calculadora.somar(3, 4));
        System.out.println(calculadora.somar(2.5, 3.5));


        // Uso do polimorfismo de sobrescrita
        Cachorro cachorro_1 = new Cachorro();
        cachorro_1.fazerSom(); 
        
        
        // Uso do polimorfismo de subtipo
        Animal cachorro_2 = new Cachorro();
        cachorro_2.fazerSom(); 
    }
}
