package edu.dio.me.functional_interfaces.examples;

import java.util.Arrays;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * Representa uma função que aceita um argumento do tipo T e retorna um resultado do tipo R.
 * É utilizada para transformar, ou mapear os elementos do Stream em outros valores, ou tipos.
 */
public class FunctionExample {
    public static void main(String[] args) {
        List<Integer> numerosDobrados;

        // Criando uma lista de números inteiros
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);


        // Usando 'Function' com expressões lambda para dobrar todos os números
        Function<Integer, Integer> dobrar = numero -> numero * 2;


        // Usando o 'Function' para imprimir os números pares no Stream
        numerosDobrados = numeros.stream()
        .map(dobrar)
        .collect(Collectors.toList());

        System.out.println("\nNúmeros dobrados:" + numerosDobrados);


        // Outra maneira:
        numerosDobrados = numeros.stream()
        .map(
            new Function<Integer, Integer> () {
                @Override
                public Integer apply(Integer n) {
                    return n * 2;
                }
            }
        ).toList();

        System.out.println("\nNúmeros dobrados:" + numerosDobrados);

        

        // Outra maneira:
        numerosDobrados = numeros.stream()
        .map( n -> n * 2)
        .toList();

        System.out.println("\nNúmeros dobrados:");
        numerosDobrados.forEach(System.out::print);
    } 
}
