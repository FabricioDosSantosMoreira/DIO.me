package edu.dio.me.exercicios;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.OptionalDouble;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3);

        // Desafio 1 - Mostre a lista na ordem numérica: Crie um programa que utilize a Stream API 
        // para ordenar a lista de números em ordem crescente e a exiba no console.
        System.out.println("\nDesafio 1:");

        List<Integer> desafio1 = numeros.stream()
            .sorted()
            .toList();

        System.out.println(desafio1);

    
        // Desafio 2 - Imprima a soma dos números pares da lista: Utilizando a Stream API, realize 
        // a soma dos números pares da lista e exiba o resultado no console.
        System.out.println("\nDesafio 2:");

        Predicate<Integer> obterPares = n -> n % 2 == 0;
        BinaryOperator<Integer> somar = Integer::sum;

        Integer desafio2 = numeros.stream()
            .filter(obterPares)
            .reduce(0, somar);
        
        System.out.println(desafio2);


        // Desafio 3 - Verifique se todos os números da lista são positivos: Com a ajuda da Stream API, 
        // verifique se todos os números da lista são positivos e exiba o resultado no console.
        System.out.println("\nDesafio 3:");

        boolean desafio3 = numeros.stream()
            .allMatch(n -> n > 0);

        System.out.println(desafio3);


        // Desafio 4 - Remova todos os valores ímpares: Utilize a Stream API para remover os valores 
        // ímpares da lista e imprima a lista resultante no console.
        System.out.println("\nDesafio 4:");

        List<Integer> desafio4 = numeros.stream()
            .filter(obterPares)
            .toList();

        System.out.println(desafio4);


        // Desafio 5 - Calcule a média dos números maiores que 5: Com a Stream API, calcule a 
        // média dos números maiores que 5 e exiba o resultado no console.
        System.out.println("\nDesafio 5:");

        Predicate<Integer> numerosMaioresQueCinco = n -> n > 5;

        OptionalDouble desafio5 = numeros.stream()
            .filter(numerosMaioresQueCinco)
            .mapToInt(Integer::intValue)
            .average();

        System.out.println(desafio5);

        // Desafio 6 - Verificar se a lista contém algum número maior que 10: Utilize a Stream API para 
        // verificar se a lista contém algum número maior que 10 e exiba o resultado no console.
        System.out.println("\nDesafio 6:");

        Predicate<Integer> numerosMaioresQueDez = n -> n > 10;

        boolean desafio6 = numeros.stream()
            .anyMatch(numerosMaioresQueDez);

        System.out.println(desafio6);


        // Desafio 7 - Encontrar o segundo número maior da lista: Com a ajuda da Stream API, encontre 
        // o segundo número maior da lista e exiba o resultado no console.
        System.out.println("\nDesafio 7:");

        Optional<Integer> desafio7 = numeros.stream()
            .distinct()                         // Remove duplicatas
            .sorted((a, b) -> b.compareTo(a))   // Ordena em ordem decrescente
            .skip(1)                          // Pula o maior
            .findFirst();                       // Pega o próximo elemento
            
        System.out.println(desafio7);


        // Desafio 8 - Somar os dígitos de todos os números da lista: Utilizando a Stream API, realize
        // a soma dos dígitos de todos os números da lista e exiba o resultado no console.
        System.out.println("\nDesafio 8:");

        Integer desafio8 = numeros.stream()
            .reduce(0, Integer::sum);
  
        System.out.println(desafio8);


        // Desafio 9 - Verificar se todos os números da lista são distintos (não se repetem): Com a Stream API, 
        // verifique se todos os números da lista são distintos e exiba o resultado no console.
        System.out.println("\nDesafio 9:");

        boolean desafio9 = numeros.stream().collect(Collectors.toSet()).size() == numeros.size();
  
        System.out.println(desafio9);


        // Desafio 10 - Agrupe os valores ímpares múltiplos de 3 ou de 5: Utilize a Stream API para agrupar 
        // os valores ímpares múltiplos de 3 ou de 5 e exiba o resultado no console.
        System.out.println("\nDesafio 10:");
        
        Predicate<Integer> numerosMultiplosDeCincoETres = n -> n % 3 == 0 || n % 5 == 0;
        Predicate<Integer> obterImpares = n -> n % 2 != 0;

        List<Integer> desafio10 = numeros.stream()
            .filter(obterImpares)
            .filter(numerosMultiplosDeCincoETres)
            .toList();

        System.out.println(desafio10);


        // Desafio 11 - Encontre a soma dos quadrados de todos os números da lista: Utilizando a Stream API, 
        // encontre a soma dos quadrados de todos os números da lista e exiba o resultado no console.
        System.out.println("\nDesafio 11:");
        
        Function<Integer, Double> paraDouble = n -> (double) n;
        Function<Double, Double> elevar = n -> Math.pow(n, 2);

        Optional<Double> desafio11 = numeros.stream()
            .map(paraDouble)
            .map(elevar)
            .reduce(Double::sum);

        System.out.println(desafio11);


        // Desafio 12 - Encontre o produto de todos os números da lista: Com a ajuda da Stream API,  
        // encontre o produto de todos os números da lista e exiba o resultado no console.
        System.out.println("\nDesafio 12:");

        BinaryOperator<Integer> obterProduto = (a, b) -> a * b;

        Optional<Integer> desafio12 = numeros.stream()
            .reduce(obterProduto);

        System.out.println(desafio12);


        // Desafio 13 - Filtrar os números que estão dentro de um intervalo: Utilize a Stream API 
        // para filtrar os números que estão dentro de um intervalo específico, entre 5 e 10 e 
        // exiba o resultado no console.
        System.out.println("\nDesafio 13:");

        Predicate<Integer> entreCincoEDez = n -> n >= 5 && n <= 10;

        List<Integer> desafio13 = numeros.stream()
            .filter(entreCincoEDez)
            .toList();
            
        System.out.println(desafio13);


        // Desafio 14 - Encontre o maior número primo da lista: Com a Stream API, encontre o maior 
        // número primo da lista e exiba o resultado no console.
        System.out.println("\nDesafio 14:");

        Predicate<Integer> obterPrimos = n -> {
            if (n <= 1) return false;
            for (int i = 2; i <= Math.sqrt(n); i++) {
                if (n % i == 0) return false;
            }
            return true;
        };

        Optional<Integer> desafio14 = numeros.stream()
            .filter(obterPrimos)
            .max(Integer::compare);
            
        System.out.println(desafio14);


        // Desafio 15 - Verifique se a lista contém pelo menos um número negativo: Utilizando a Stream API, 
        // verifique se a lista contém pelo menos um número negativo e exiba o resultado no console.
        System.out.println("\nDesafio 15:");

        Predicate<Integer> verificarNegativo = n -> n < 0;

        boolean desafio15 = numeros.stream()
            .anyMatch(verificarNegativo);            

        System.out.println(desafio15);


        // Desafio 16 - Agrupe os números em pares e ímpares: Utilize a Stream API para agrupar os números 
        // em duas listas separadas, uma contendo os números pares e outra contendo os números ímpares da 
        // lista original, e exiba os resultados no console.
        System.out.println("\nDesafio 16:");

        List<Integer> desafio16Pares = numeros.stream()
            .filter(obterPares)
            .toList();
            
        List<Integer> desafio16Impares = numeros.stream()
        .filter(obterImpares)
        .toList();

        System.out.println(desafio16Pares);
        System.out.println(desafio16Impares);


        // Desafio 17 - Filtrar os números primos da lista: Com a ajuda da Stream API, filtre os 
        // números primos da lista e exiba o resultado no console.
        System.out.println("\nDesafio 17:");

        List<Integer> desafio17 = numeros.stream()
            .filter(obterPrimos)
            .toList();

        System.out.println(desafio17);


        // Desafio 18 - Verifique se todos os números da lista são iguais: Utilizando a Stream API, 
        // verifique se todos os números da lista são iguais e exiba o resultado no console.
        System.out.println("\nDesafio 18:");

        boolean desafio18 = numeros.stream()
            .allMatch(n -> n.equals(numeros.get(0)));

        System.out.println(desafio18);


        // Desafio 19 - Encontre a soma dos números divisíveis por 3 e 5: Com a Stream API, 
        // encontre a soma dos números da lista que são divisíveis tanto por 3 quanto por 5 
        // e exiba o resultado no console.
        System.out.println("\nDesafio 19:");

        Predicate<Integer> divisiveisPorTresECinco = n -> n % 3 == 0 || n % 5 == 0;

        Optional<Integer> desafio19 = numeros.stream()
            .filter(divisiveisPorTresECinco)
            .reduce(somar);

        System.out.println(desafio19);
    }
}
