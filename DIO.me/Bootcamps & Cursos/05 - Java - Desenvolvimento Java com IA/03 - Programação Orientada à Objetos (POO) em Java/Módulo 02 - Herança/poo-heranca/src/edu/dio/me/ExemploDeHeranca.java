package edu.dio.me;

public class ExemploDeHeranca {

    // - - - - - > Herança:
    //                 A herança é um dos princípios fundamentais da programação orientada a objetos (POO)
    //             em Java. Ela é usada para que uma classe herde características (atributos e métodos) de 
    //             outra classe, reutilizando código e criando uma hierarquia entre classes.

    public static void main(String[] args) {
        
        // Criando um objeto da classe 'Pessoa'
        Cachorro cachorro = new Cachorro();
        
        // Modificando os atributos do objeto que foi herdado da superclasse
        cachorro.nome = "Cookie";
        cachorro.idade = 3;

        System.out.println("Nome: " + cachorro.nome);
        System.out.println("Idade: " + cachorro.idade);
        
        // Usando o método sobrescrito da subclasse
        cachorro.emitirSom(); 
        
        // Usando o método específico da subclasse
        cachorro.latir(); 
    }
}
