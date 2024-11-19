package edu.dio.me;

// Classe derivada ou subclasse que herda de 'Animal'
public class Cachorro extends Animal {
    
    // Novo método específico da subclasse 'Cachorro'
    void latir() {
        System.out.println("O cachorro está latindo.");
    }

    // Sobrescrevendo o método da classe base 'Animal'
    @Override
    void emitirSom() {
        System.out.println("O cachorro faz au au.");
    }
}