// ├───┬───> Exercício: Ordenação de Números
// │   │
// │   └───>    Crie uma classe chamada "OrdenacaoNumeros" que possui uma lista de números inteiros como atributo.
// │         Implemente os seguintes métodos:
// │
// │            * adicionarNumero(int numero): Adiciona um número à lista.
// │            * ordenarCrescente(): Ordena os números da lista em ordem ascendente usando a interface Comparable e a class Collections.
// │            * ordenarDecrescente(): Ordena os números da lista em ordem descendente usando um Comparable e a class Collections.
// │
// │
// │
// └───────> Código:


package List.Exercicios.Ordenacao.OrdenacaoDeNumeros;

import java.util.List;
import java.util.Random;


public class Main {
    public static void main(String[] args) {

        // Instânciando um objeto da classe 'OrdenacaoNumeros'
        OrdenacaoNumeros numeros = new OrdenacaoNumeros();

        // Instânciando um objeto da classe 'Random'
        Random random = new Random();

        // Adicionando números aleatórios
        for (int i = 0; i <= 10; i++) {
            numeros.adicionarNumero(random.nextInt(0, 1000));
        }

        // Exibindo a lista de números
        System.out.print("\nLista de números: ");
        numeros.exibirNumeros();

        // Exibindo a lista de números em ordem crescente
        List<Integer> numerosCrescente = numeros.ordenarCrescente();
        System.out.print("\nLista de números em ordem crescente: ");
        System.out.println(numerosCrescente);

        // Exibindo a lista de números em ordem decrescente
        List<Integer> numerosDecrescente = numeros.ordenarDecrescente();
        System.out.print("\nLista de números em ordem decrescente: ");
        System.out.println(numerosDecrescente);
    }
}
