package edu.dio.me.optional;

import java.util.Optional;

public class Main {

    // - - - - -> Optional:
    //                A classe Optional em Java é uma classe de contêiner que pode 
    //            conter ou não um valor não nulo. Ela foi introduzida no Java 8 
    //            como parte do pacote java.util e é usada principalmente para 
    //            evitar o uso de null e para lidar com valores que podem estar 
    //            ausentes de uma maneira mais segura e expressiva.
    //
    // - - - -> Principais Características da classe 'Optional':
    //
    // - - -> Criação de um 'Optional':
    //
    //            -> 'Optional.of(T value)': Cria um Optional contendo o valor fornecido. 
    //                Lança uma exceção NullPointerException se o valor for null.
    //
    //            -> 'Optional.ofNullable(T value)': Cria um Optional contendo o valor 
    //                fornecido, ou um Optional vazio se o valor for null.
    //
    //            -> 'Optional.empty()': Cria um Optional vazio.
    //
    // - - -> Verificação de presença de valor:
    //
    //            -> 'boolean isPresent()': Retorna true se houver um valor presente, 
    //                caso contrário, retorna false.
    //
    //            -> 'boolean isEmpty()': Retorna true se não houver um valor presente, 
    //                caso contrário, retorna false.
    //
    // - - -> Recuperação de valor:
    //
    //            -> 'T get()': Retorna o valor se presente, caso contrário, lança 
    //               uma exceção NoSuchElementException.
    //
    //            -> 'T orElse(T other)': Retorna o valor se presente, caso contrário, 
    //                retorna other.
    //
    //            -> 'T orElseGet(Supplier<? extends T> supplier)': Retorna o valor se presente, 
    //                caso contrário, invoca o supplier e retorna o resultado.
    //
    //            -> 'T orElseThrow()': Retorna o valor se presente, caso contrário, lança uma 
    //                exceção NoSuchElementException.
    //
    //            -> 'T orElseThrow(Supplier<? extends X> exceptionSupplier)': Retorna o valor 
    //                se presente, caso contrário, lança uma exceção criada pelo exceptionSupplier.
    //
    // - - -> Ações condicionais:
    //
    //            -> 'void ifPresent(Consumer<? super T> action)': Executa a ação fornecida se um valor 
    //                estiver presente.
    //
    //            -> 'Optional<T> filter(Predicate<? super T> predicate)': Retorna um Optional contendo 
    //                o valor se o valor estiver presente e corresponder ao predicate, caso contrário, 
    //                retorna um Optional vazio.
    //
    // - - -> Transformações:
    //
    //            -> '<U> Optional<U> map(Function<? super T, ? extends U> mapper)': Se um valor estiver 
    //               presente, aplica a função fornecida e, se o resultado não for nulo, retorna um 
    //               Optional contendo o resultado. Caso contrário, retorna um Optional vazio.
    //
    //            -> '<U> Optional<U> flatMap(Function<? super T, Optional<U>> mapper)': Similar ao map, 
    //               mas a função retornada também é um Optional, e evita a necessidade de aninhamento de 
    //               Optional.

    public static void main(String[] args) {
        
        // Criando um 'Optional' com 'Optional.of()'
        Optional<String> optionalOfValue = Optional.of("Value");

        // Criando um 'Optional' com 'Optional.ofNullable()'
        String nullableValue = null;
        Optional<String> optionalOfNullableValue = Optional.ofNullable(nullableValue);

        // Criando um 'Optional' com 'Optional.empty()'
        Optional<String> optionalEmptyValue = Optional.empty();



        // Verificando um 'Optional' com 'isPresent()'
        System.out.println(optionalOfValue.isPresent());
        System.out.println(optionalOfNullableValue.isPresent());
        System.out.println(optionalEmptyValue.isPresent());

        // Verificando um 'Optional' com 'isEmpty()'
        System.out.println(optionalOfValue.isEmpty());
        System.out.println(optionalOfNullableValue.isEmpty());
        System.out.println(optionalEmptyValue.isEmpty());



        // Recuperando valores de um 'Optional' com 'get()'
        System.out.println(optionalOfValue.get());
        // OBS: Lançará uma exceção, pois não há valores
        // System.out.println(optionalOfNullableValue.get());
        // System.out.println(optionalEmptyValue.get());

        // Recuperando valores de um 'Optional' com 'orElse()'
        System.out.println(optionalOfValue.orElse("Default Value"));
        System.out.println(optionalOfNullableValue.orElse("Default Value"));
        System.out.println(optionalEmptyValue.orElse("Default Value"));

        // Recuperando valores de um 'Optional' com 'orElseGet()'
        String result;

        result = optionalOfValue.orElseGet(() -> "Value from Supplier");
        System.out.println(result);
        result = optionalOfNullableValue.orElseGet(() -> "Value from Supplier");
        System.out.println(result);
        result = optionalEmptyValue.orElseGet(() -> "Value from Supplier");
        System.out.println(result);

        // Recuperando valores de um 'Optional' com 'orElseThrow()'
        result = optionalOfValue.orElseThrow(() -> new RuntimeException("Value not present"));
        // OBS: Lançará uma exceção, pois não há valores
        // result = optionalOfNullableValue.orElseThrow(() -> new RuntimeException("Value not present"));
        // result = optionalEmptyValue.orElseThrow(() -> new RuntimeException("Value not present"));



        // Usando 'ifPresent' para executar uma ação se o 'Optional' tiver um valor
        optionalOfValue.ifPresent(val -> System.out.println("Value is present: " + val));
        optionalOfNullableValue.ifPresent(val -> System.out.println("Value is present: " + val));
        optionalEmptyValue.ifPresent(val -> System.out.println("Value is present: " + val));

        // Usando 'filter' para obter um 'Optional' filtrado
        Optional<String> filteredValue;

        filteredValue = optionalOfValue.filter(val -> val.startsWith("Val"));
        filteredValue.ifPresent(val -> System.out.println("Filtered value: " + val)); 

        filteredValue = optionalOfNullableValue.filter(val -> val.startsWith("Val"));
        filteredValue.ifPresent(val -> System.out.println("Filtered value: " + val)); 

        filteredValue = optionalEmptyValue.filter(val -> val.startsWith("Val"));
        filteredValue.ifPresent(val -> System.out.println("Filtered value: " + val)); 


        // Transformando valores de um 'Optional' com 'map()'
        System.out.println(optionalOfValue.map(String::length));

        System.out.println(optionalOfValue.map(String::toUpperCase));

        // Transformando valores de um 'Optional' com 'flatmap()'
        System.out.println(optionalOfValue.flatMap(value -> Optional.of(value.length())));
     
        System.out.println(optionalOfValue.flatMap(value -> Optional.of(value.toUpperCase())));
    }
}

