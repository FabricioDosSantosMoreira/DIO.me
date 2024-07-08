package edu.me.poo.interfaces;

// A herança não pode ser multipla EX. classeA extends casseB, ClasseC.
// Mas a interface pode ser multipla Ex. ClasseA extends IntefaceA, InterfaceB



// Em Java, uma classe pode estender apenas uma única classe diretamente. Isso significa que Java não suporta herança múltipla direta, onde uma classe herda diretamente de mais de uma classe pai. No entanto, é possível implementar múltiplas interfaces em uma classe, o que permite alcançar um comportamento semelhante ao da herança múltipla para tipos de comportamento.

// Por exemplo, em Java:

// java
// Copiar código
// public class MinhaClasse extends ClassePai {
//     // código da classe
// }
// Aqui, MinhaClasse está estendendo ClassePai, e isso é a única herança direta permitida.

// Para utilizar múltiplos comportamentos de várias fontes, você pode implementar múltiplas interfaces:

// java
// Copiar código
// public class MinhaClasse implements Interface1, Interface2 {
//     // código da classe
// }
// Isso permite que MinhaClasse implemente comportamentos definidos em Interface1 e Interface2, sem herdar diretamente de múltiplas classes pai.




public class Main {
    public static void main(String[] args) {
        
    }
}


// Exemplo de interface
interface Animal {
    // Métodos abstratos
    void emitirSom();
    void mover();
}

// Implementação da interface
class Cachorro implements Animal {
    @Override
    public void emitirSom() {
        System.out.println("Au au!");
    }
    
    @Override
    public void mover() {
        System.out.println("Correndo");
    }
}

