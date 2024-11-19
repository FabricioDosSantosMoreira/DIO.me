package edu.dio.me;

public class ExemploDeEncapsulamento {

    // - - - - - > Encapsulamento:
    //                 O encapsulamento é um dos princípios fundamentais da programação orientada a objetos (POO)
    //             em Java. Ele é usado para proteger os dados de uma classe, garantindo que o acesso a esses 
    //             dados seja controlado e seguro. O encapsulamento é realizado através do uso dos métodos
    //             'getters' e 'setters' e dos modificadores de acesso 'private', 'protected' e 'public'.

    public static void main(String[] args) {
        
        // Criando um objeto da classe 'Pessoa'
        Pessoa pessoa = new Pessoa("Pessoa", 0);

        // Modificando os atributos pelos métodos 'setter'
        pessoa.setNome("Fabrício");
        pessoa.setIdade(20);

        // Exibindo os atributos pelos métodos 'getter'
        System.out.println("Nome: " + pessoa.getNome());
        System.out.println("Idade: " + pessoa.getIdade());
    }
}
 