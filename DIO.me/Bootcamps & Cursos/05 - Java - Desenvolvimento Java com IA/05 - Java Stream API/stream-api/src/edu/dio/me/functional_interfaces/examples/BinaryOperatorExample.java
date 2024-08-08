package edu.dio.me.functional_interfaces.examples;

import java.util.Arrays;
import java.util.List;
import java.util.function.BinaryOperator;

/**
 * Representa uma operação que combina dois argumentos do tipo T e retorna um resultado do mesmo tipo T.
 * É usada para realizar operações de redução em pares de elementos, como somar números ou combinar objetos.
 */
public class BinaryOperatorExample {
    public static void main(String[] args) {
        int resultado;

        // Criando uma lista de números inteiros
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5);


        // Usando o 'BinaryOperator' com expressão lambda para somar dois números inteiros
        BinaryOperator<Integer> somar = Integer::sum;
        // Ou, BinaryOperator<Integer> somar = (num1, num2) -> num1 + num2;


        // Usando o 'BinaryOperator' para somar todos os números no Stream
        resultado = numeros.stream()
            .reduce(0, somar);

        System.out.println("\nResultado da soma: " + resultado);

        // Outra maneira:
        resultado = numeros.stream()
        .reduce(0, Integer::sum);

        System.out.println("\nResultado da soma: " + resultado);

        // Outra maneira:
        resultado = numeros.stream()
        .reduce(0, 
        new BinaryOperator <Integer> () {
            @Override 
            public Integer apply(Integer num1, Integer num2) {
                return num1 + num2;
            }
        });

        System.out.println("\nResultado da soma: " + resultado);

        // Outra maneira:
        resultado = numeros.stream()
        .reduce(0, (n1, n2) -> n1 + n2);

        System.out.println("\nResultado da soma: " + resultado);
    }
}
