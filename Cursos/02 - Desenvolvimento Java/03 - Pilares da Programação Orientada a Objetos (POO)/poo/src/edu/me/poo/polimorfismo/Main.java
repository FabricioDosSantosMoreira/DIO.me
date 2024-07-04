package edu.me.poo.polimorfismo;


public class Main {
    public static void main(String[] args) {

        // Uso do polimorfismo
        Animal animal = new Cachorro();
        animal.fazerSom(); // Saída: "Au au!"

        // Uso do polimorfismo por sobrecarga
        Calculadora calc = new Calculadora();
        System.out.println(calc.somar(3, 4)); // Saída: 7
        System.out.println(calc.somar(2.5, 3.5)); // Saída: 6.0

    }
}




// Polimorfismo de Sobrescrita (Override): Ocorre quando uma subclasse fornece uma implementação específica de um método que já está sendo implementado por sua superclasse. Isso permite que um objeto de qualquer classe derivada use o método que ele "sobrescreveu".
abstract class Animal {
    void fazerSom() {
        System.out.println("Som genérico de um animal");
    }
}

class Cachorro extends Animal {
    @Override
    void fazerSom() {
        System.out.println("Au au!");
    }
}


//Polimorfismo de Sobrecarga (Overload): Refere-se à capacidade de uma classe ter dois ou mais métodos com o mesmo nome, mas com listas de parâmetros diferentes. O compilador Java escolhe qual método chamar com base na lista de argumentos fornecida
class Calculadora {
    public int somar(int a, int b) {
        return a + b;
    }
    
    public double somar(double a, double b) {
        return a + b;
    }
}
