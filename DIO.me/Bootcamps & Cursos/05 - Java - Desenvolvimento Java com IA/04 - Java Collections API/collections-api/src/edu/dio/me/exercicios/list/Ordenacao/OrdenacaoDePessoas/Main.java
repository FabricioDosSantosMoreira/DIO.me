// ├───────> Exercício - Ordenação de Pessoas:
// │             Crie uma classe chamada 'OrdenacaoPessoas' que possui uma lista de objetos 
// │         do tipo 'Pessoa' como atributo. Cada pessoa possui atributos como nome, idade 
// │         e altura. Implemente os seguintes métodos:
// │
// │            * adicionarPessoa(String nome, int idade, double altura): 
// │                  Adiciona uma pessoa à lista.
// │
// │            * ordenarPorIdade(): 
// │                  Ordena as pessoas da lista por idade usando a interface Comparable.
// │
// │            * ordenarPorAltura(): 
// │                 Ordena as pessoas da lista por altura usando um Comparator personalizado.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.list.Ordenacao.OrdenacaoDePessoas;

public class Main {
    
    public static void main(String[] args) {

        // Instânciando um objeto da classe 'OrdenacaoPessoas'
        OrdenacaoPessoas pessoas = new OrdenacaoPessoas();
        
        // Adicionando pessoas 
        pessoas.adicionarPessoa("Alice", 20, 1.56);
        pessoas.adicionarPessoa("Bob", 30, 1.80);
        pessoas.adicionarPessoa("Charlie", 25, 1.70);
        pessoas.adicionarPessoa("David", 17, 1.56);

        // Exibindo a lista de pessoas
        System.out.println(pessoas.getPessoas());

        // Ordenando e exibindo por idade
        System.out.println("\nOrdenando por idade");
        System.out.println(pessoas.ordenarPorIdade());

        // Ordenando e exibindo por altura
        System.out.println("\nOrdenando por altura");
        System.out.println(pessoas.ordenarPorAltura());
    }
}
