package edu.dio.me.functional_interfaces.examples;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

/**
 * Representa uma função que aceita um argumento do tipo T e retorna um valor booleano (verdadeiro ou falso).
 * É comumente usada para filtrar os elementos do Stream com base em alguma condição.
 */
public class PredicateExample {
    public static void main(String[] args) {

        // Criando uma lista de palavras
        List<String> palavras = Arrays.asList("java", "kotlin", "python", "javascript", "c", "go", "ruby");


        // Criando um 'Predicate' que verifica se a palavra tem mais de 5 caracteres
        Predicate<String> maisDeCincoCaracteres = palavra -> palavra.length() > 5;


        // Usando o Stream para filtrar as palavras com mais de 5 caracteres e, em seguida,
        // imprimir cada palavra que passou no filtro
        System.out.println("\nPalavras com mais de 5 caracteres:");

        palavras.stream()
        .filter(maisDeCincoCaracteres)
        .forEach(System.out::println);


        // Outra maneira:
        System.out.println("\nPalavras com mais de 5 caracteres:");

        palavras.stream()
        .filter(
            new Predicate<String>() {
                public boolean test(String p) {
                    return p.length() > 5;
                }
            }
        ).forEach(System.out::println);

        // Outra maneira:
        System.out.println("\nPalavras com mais de 5 caracteres:");

        palavras.stream()
        .filter(p -> p.length() > 5).forEach(System.out::println);
    }
}
