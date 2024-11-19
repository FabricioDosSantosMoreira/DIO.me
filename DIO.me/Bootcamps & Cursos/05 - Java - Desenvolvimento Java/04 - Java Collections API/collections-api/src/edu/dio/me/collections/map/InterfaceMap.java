package edu.dio.me.collections.map;

public class InterfaceMap {

    // - - - - -> Interface Map:
    //                A interface Map é usada para mapear dados na forma de chaves e valores. O Map 
    //            do Java é um objeto que mapeia chaves para valores. Um Map não pode conter chaves 
    //            duplicadas, ou seja, cada chave pode mapear no máximo um valor.
    //
    // - - - -> HashTable: 
    //              O HashTable é uma implementação antiga da interface Map no Java que é sincronizada 
    //          e thread-safe, tornando-a adequada para uso em ambientes concorrentes. Ela não permite 
    //          chaves ou valores nulos e os elementos não são mantidos em uma ordem específica.
    //
    // - - - -> LinkedHashMap:
    //              O LinkedHashMap é uma implementação da interface Map que preserva a ordem de inserção 
    //          dos elementos. Cada elemento possui referências ao próximo e ao anterior, formando uma 
    //          lista encadeada. Isso permite que os elementos sejam iterados na ordem em que foram 
    //          inseridos. Além disso, o LinkedHashMap também permite chaves ou valores nulos.
    //
    // - - - -> HashMap: 
    //              O HashMap é uma implementação da interface Map que não mantém uma ordem específica dos 
    //          elementos. Ele armazena os elementos internamente usando uma função de hash para melhorar 
    //          a eficiência das operações de pesquisa e acesso. O HashMap também permite chaves ou 
    //          valores nulos.

    public static void main(String[] args) {
        
    }
}
