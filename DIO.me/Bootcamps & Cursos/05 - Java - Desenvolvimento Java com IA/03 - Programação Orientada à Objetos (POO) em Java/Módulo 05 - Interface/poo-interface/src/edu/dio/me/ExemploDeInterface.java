package edu.dio.me;

public class ExemploDeInterface {

    // - - - - - > Interface:
    //                 A Interface é dos princípios fundamentais da programação orientada a objetos (POO) 
    //             em Java. Ela se refere à um tipo de referência que pode conter apenas constantes, 
    //             assinaturas de métodos (sem corpo), e métodos 'default' e 'static'. Interfaces 
    //             permitem definir um contrato que outras classes podem implementar. 
    //
    // - - - - > métodos de Interface:
    //
    // - - - > Métodos default: 
    //             fornecem uma implementação padrão que as classes podem usar ou sobrescrever. 
    //
    // - - - > Métodos static: 
    //             pertencem à interface e não à instância da classe.
    // 
    // NOTE: Em Java, uma classe pode estender apenas uma única classe diretamente. Isso significa
    //       que o Java não suporta herança múltipla direta, onde uma classe herda diretamente de 
    //       mais de uma classe pai. No entanto, é possível implementar múltiplas interfaces em
    //       uma classe, o que permite alcançar um comportamento semelhante ao da herança
    //       múltipla para tipos de comportamento.
    
    public static void main(String[] args) {

        // Criando um objeto da classe 'Carro'
        Carro carro = new Carro();
        
        // Usando o método 'static'
        Veiculo.abastecer();

        // Usando o método 'default'
        carro.ligar();

        // Usando o método sobrescrito
        carro.navegar();
    }
}
