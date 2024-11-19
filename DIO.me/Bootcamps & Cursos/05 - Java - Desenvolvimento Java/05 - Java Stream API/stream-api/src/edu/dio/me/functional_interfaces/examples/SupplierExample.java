package edu.dio.me.functional_interfaces.examples;

import java.util.List;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * Representa uma operação que não aceita nenhum argumento e retorna um resultado do tipo T.
 * É comumente usada para criar ou fornecer novos objetos de um determinado tipo.
 */
public class SupplierExample {
    public static void main(String[] args) {
        List<String> listaSaudacoes ;
        
        // Usando o  'Supplier' com expressão lambda para fornecer uma saudacao personalizada
        Supplier<String> saudacao = () -> "Olá, seja bem-vindo(a)";

    
        // Usando o 'Supplier' para obter uma lista com 5 saudacoes
        listaSaudacoes = Stream.generate(saudacao)
            .limit(5)
            .collect(Collectors.toList()); // Ou .toList()

        listaSaudacoes.forEach(s -> System.out.println(s));

        // Outra maneira:
        listaSaudacoes = Stream.generate(
            new Supplier<String>() {
                @Override
                public String get() {
                    return "Olá, seja bem-vindo(a)";
                }
            }
        ).limit(5).toList();

        listaSaudacoes.forEach(s -> System.out.println(s));

        // Outra maneira:
        listaSaudacoes = Stream.generate(() -> "Olá, seja bem-vindo(a)")
            .limit(5)
            .toList();

        listaSaudacoes.forEach(s -> System.out.println(s));
    }   
}
