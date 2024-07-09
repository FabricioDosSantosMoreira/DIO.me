package functional_inteface.examples;

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
        
        // Usa o  Supplie com expressão lambda para fornecer uma saudacao personalizada
        Supplier<String> saudacao = () -> "Olá, seja bem-vindo(a)";

    
        // Usa o Supplier para obter uma lista com 5 saudacoes
        List<String> listaSaudacoes = Stream.generate(saudacao)
            .limit(5)
            .collect(Collectors.toList());    
            // Ou .toList()

        // // Ou
        // List<String> listaSaudacoes = Stream.generate(
        //     new Supplier<String>() {
        //         @Override
        //         public String get() {
        //             return "Olá, seja bem-vindo(a)";
        //         }
        //     }
        // ).limit(5).toList();


        // // Ou
        // List<String> listaSaudacoes = Stream.generate(() -> "Olá, seja bem-vindo(a)")
        //     .limit(5)
        //     .toList();




        // Imprimindo 
        listaSaudacoes.forEach(s -> System.out.println(s));
    
        // method reference
        listaSaudacoes.forEach(System.out::println);
    }   
}
