package edu.dio.me.functional_interfaces.examples;

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

/**
 * Representa uma operação que aceita um argumento do tipo T e não retorna nenhum resultado.
 * É utilizada principalmente para realizar ações, ou efeitos colaterais nos elementos do Stream sem modificar, ou
 * retornar um valor.
 */
public class ConsumerExample {
    public static void main(String[] args) {
        
        // Criando uma lista de números inteiros
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);


        // Usando o 'Consumer' com expressões lambda para imprimir números pares
        Consumer<Integer> imprimirNumeroPar = numero -> {
            if (numero % 2 == 0) {
                System.out.print(numero + " ");
            }
        };
    
        // Usando o 'Consumer' para imprimir os números pares no Stream
        System.out.println("\nNúmeros pares: ");
        numeros.stream().forEach(imprimirNumeroPar);


        // Outra maneira:
        System.out.println("\nNúmeros pares: ");
        numeros.stream().forEach(new Consumer<Integer>() {
            @Override
            public void accept(Integer n) {
                if(n % 2 == 0) {
                    System.out.print(n + " ");
                }
            }
        });

        // Outra maneira:
        System.out.println("\nNúmeros pares: ");
        numeros.forEach(n -> {
            if(n % 2 ==0) {
                System.out.print(n + " ");
            }
        });

        // Outra maneira:
        System.out.println("\nNúmeros pares: ");
        numeros.stream()
        .filter(n -> n % 2 == 0)
        .forEach(System.out::print);
    }
}
 