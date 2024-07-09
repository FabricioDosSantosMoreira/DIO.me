/**
 * Representa uma operação que aceita um argumento do tipo T e não retorna nenhum resultado.
 * É utilizada principalmente para realizar ações, ou efeitos colaterais nos elementos do Stream sem modificar, ou
 * retornar um valor.
 */
package functional_inteface.examples;


import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;


public class ConsumerExample {
    public static void main(String[] args) {
        
        // Cria uma lista de números inteiros
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);

        System.out.println("\n");
        // Usa o 'Consumer' com expressões lambda para imprimir números pares
        Consumer<Integer> imprimirNumeroPar = numero -> {
            if (numero % 2 == 0) {
                System.out.print(numero + " ");
            }
        };
    
        // Usa o 'Consumer' para imprimir os números pares no Stream
        numeros.stream().forEach(imprimirNumeroPar);

        System.out.println("\n");
        // outra maneira
        numeros.stream().forEach(new Consumer<Integer>() {
            @Override
            public void accept(Integer n) {
                if(n % 2 == 0) {
                    System.out.print(n + " ");
                }
            }
        });

        System.out.println("\n");
        // Outra maneira
        numeros.forEach(n -> {
            if(n % 2 ==0) {
                System.out.print(n + " ");
            }
        });



        // Ou usando um Predicate -> ver no PredicateExample outros exemplos
        numeros.stream()
        .filter(n -> n % 2 == 0)
        .forEach(System.out::println);
    }
}
 