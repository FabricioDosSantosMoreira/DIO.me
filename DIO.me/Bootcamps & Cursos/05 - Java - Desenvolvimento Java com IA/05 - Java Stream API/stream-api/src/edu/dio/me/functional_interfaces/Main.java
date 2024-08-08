package edu.dio.me.functional_interfaces;

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    // - - - - -> Stream API:
    //                A Stream API em Java foi introduzida no Java 8 e fornece uma 
    //            maneira funcional de processar sequências de elementos. Ela permite 
    //            realizar operações como filtragem, mapeamento e redução de maneira 
    //            declarativa e eficiente.
    //
    // - - - -> Principais Características da Stream API:
    //
    // - - -> Criação de uma Stream:
    //
    //            -> 'Stream.of(T... values)': Cria uma stream a partir de uma sequência de valores.
    //
    //            -> 'Arrays.stream(T[] array)': Cria uma stream a partir de um array.
    //
    //            -> 'List.stream()': Cria uma stream a partir de uma lista.
    //
    // - - -> Operações intermediárias:
    //
    //            -> 'filter(Predicate<? super T> predicate)': Filtra os elementos da stream 
    //                com base em um predicado.
    //
    //            -> 'map(Function<? super T, ? extends R> mapper)': Transforma os elementos 
    //                da stream aplicando uma função.
    //
    //            -> 'sorted()': Ordena os elementos da stream.
    //
    //            -> 'distinct()': Remove elementos duplicados da stream.
    //
    //            -> 'limit(long maxSize)': Limita o tamanho da stream.
    //
    //            -> 'skip(long n)': Pula os primeiros n elementos da Stream. 
    //
    // - - -> Operações terminais:
    //
    //            -> 'forEach(Consumer<? super T> action)': Executa uma ação para cada elemento da stream.
    //
    //            -> 'collect(Collector<T, A, R> collector)': Coleta os elementos da Stream em uma estrutura de 
    //               dados específica, como uma lista ou um mapa. 
    //
    //            -> 'anyMatch(Predicate<T> predicate)': Verifica se algum elemento da Stream atende ao 
    //               predicado especificado.
    //
    //            -> 'allMatch(Predicate<T> predicate)': Verifica se todos os elementos da Stream atendem 
    //               ao predicado especificado. 
    //
    //            -> 'noneMatch(Predicate<T> predicate)': Verifica se nenhum elemento da Stream atende ao 
    //               predicado especificado. 
    //
    //            -> 'min(Comparator<T> comparator)': Encontra o elemento mínimo da Stream. de acordo com o 
    //                comparador fornecido.
    //
    //            -> 'max(Comparator<T> comparator)': Encontra o elemento máximo da Stream, de acordo com o 
    //               comparador fornecido.
    //
    //            -> 'reduce(T identity, BinaryOperator<T> accumulator)': Combina os elementos da Stream 
    //               usando o acumulador especificado e retorna o resultado final.
    //
    //            -> 'count()': Retorna o número de elementos na stream.
    //
    //            -> 'findFirst()': Retorna o primeiro elemento da stream, se presente.
    //
    //
    // - - -> Interfaces funcionais:
    //
    //            -> 'Predicate<T>': Representa um predicado (função que retorna booleano).
    //
    //            -> 'Function<T, R>': Representa uma função que aceita um argumento e produz 
    //               um resultado.
    //
    //            -> 'Consumer<T>': Representa uma operação que aceita um único argumento e não 
    //               retorna resultado.
    //
    //            -> 'Supplier<T>': Representa uma função que fornece um resultado sem 
    //               aceitar argumentos.
    //
    //            -> 'UnaryOperator<T>': Representa uma função que aceita um argumento e 
    //               produz um resultado do mesmo tipo.
    //
    //            -> 'BinaryOperator<T>': Representa uma função que aceita dois argumentos e 
    //               produz um resultado do mesmo tipo.
    //
    // - - -> Method References:
    //
    //            -> São uma forma mais concisa de escrever lambdas que chamam métodos existentes.
    //
    //            -> 'Class::staticMethod': Referência a um método estático.
    //
    //            -> 'instance::instanceMethod': Referência a um método de instância.
    //
    //            -> 'Class::new': Referência a um construtor.
    //
    // - - -> Lambdas:
    //
    //            -> São uma forma compacta de representar uma função anônima que pode ser passada como argumento.
    //
    //            -> Sintaxe: '(parameters) -> expression' ou '(parameters) -> { statements; }'
    
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");

        // Criação de uma Stream a partir de uma lista
        Stream<String> streamOfNames = names.stream();

        // Uso de filter (com Predicate) para filtrar nomes que começam com 'A'
        Stream<String> filteredNames = streamOfNames.filter(name -> name.startsWith("A"));

        // Uso de map (com Function) para transformar nomes em letras maiúsculas
        Stream<String> upperCaseNames = filteredNames.map(String::toUpperCase);

        // Coleta os nomes resultantes em uma lista
        List<String> result = upperCaseNames.collect(Collectors.toList());

        // Impressão dos resultados
        System.out.println(result);

        // Operações intermediárias e terminais encadeadas
        List<String> processedNames = names.stream()
            .filter(name -> name.length() > 3)
            .map(String::toUpperCase)
            .sorted()
            .distinct()
            .collect(Collectors.toList());

        // Impressão dos resultados
        System.out.println(processedNames);

        // Uso de forEach (com Consumer) para imprimir cada nome
        names.forEach(System.out::println);

        // Uso de count para contar o número de elementos na stream
        long count = names.stream().count();
        System.out.println("Count: " + count);

        // Uso de findFirst para encontrar o primeiro elemento na stream
        names.stream().findFirst().ifPresent(name -> System.out.println("First: " + name));

        // Exemplos de interfaces funcionais
        Predicate<String> startsWithA = name -> name.startsWith("A");
        Function<String, Integer> stringLength = String::length;
        Consumer<String> printName = System.out::println;

        // Uso de Predicate para filtrar nomes
        List<String> filtered = names.stream()
            .filter(startsWithA)
            .collect(Collectors.toList());
        System.out.println(filtered);

        // Uso de Function para mapear nomes para seus comprimentos
        List<Integer> lengths = names.stream()
            .map(stringLength)
            .collect(Collectors.toList());
        System.out.println(lengths);

        // Uso de Consumer para imprimir nomes
        names.forEach(printName);
    }
}
