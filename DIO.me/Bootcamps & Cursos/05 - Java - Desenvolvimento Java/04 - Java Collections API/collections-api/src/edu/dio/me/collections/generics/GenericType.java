package edu.dio.me.collections.generics;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.Set;

public class GenericType {

    // - - - - -> Generic Type:
    //                Um tipo genérico é uma classe genérica ou uma interface que é parametrizada
    //            em relação a tipos. Sendo que, uma variável de tipo pode ser qualquer tipo não 
    //            primitivo especificado. Quanto aos nomes de parâmetros de tipo mais comumente 
    //            usados temos:
    //
    //                -> E - Elemento (usado extensivamente pelo Java Collections Framework)
    //                -> K - Chave
    //                -> N - Número
    //                -> T - Tipo
    //                -> V - Valor
    //                -> S, U, V, etc. - 2º, 3º, 4º tipos
    //
    // - - - -> Vantagens dos Generic Type:
    //       
    //              -> Segurança do tipo de dados: O uso de generics garante que apenas objetos de um 
    //                 tipo específico possam ser adicionados à coleção, evitando erros de tipo.
    //
    //              -> Código legível: Ao usar generics, é possível especificar o tipo de dados esperado 
    //              ou retornado pela coleção, o que torna o código mais fácil de entender e ler.
    //
    //              -> Detecção de erros mais cedo: O compilador verifica se você está usando os tipos 
    //                 corretos durante a compilação, ajudando a identificar erros de tipo antes mesmo 
    //                 de executar o programa.
    //
    //              -> Reutilização de código: Com generics, é possível criar classes e métodos genéricos 
    //              que funcionam com diferentes tipos de coleções, evitando a necessidade de duplicar 
    //              código para cada tipo específico.
    //
    //              -> Melhor desempenho: O uso de generics pode melhorar o desempenho, pois evita a 
    //                 necessidade de conversões de tipo desnecessárias e permite que o compilador 
    //                 otimize o código com base no tipo especificado.
    //
    // - - - -> Classe 'Box' sem Generics:
    //
    //          public class Box {
    //              private Object object;
    //              public void set(Object object) { this.object = object; }
    //              public Object get() { return object; }
    //          }
    //
    // - - - -> Classe 'Box' com Generics:
    //
    //          public class Box<T> {    OBS: '<T>' sendo o tipo
    //              private T t;
    //              public void set(T t) { this.t = t; }
    //              public T get() { return t; }
    //          }

    @SuppressWarnings({ "unused" })
    public static void main(String[] args) {
        
        // Exemplos de 'collections' com 'Generic Type':
        List<String> listaStrings = new ArrayList<>();
        List<Integer> listaIntegers = new ArrayList<>();
        List<Float> listaFloats = new ArrayList<>();

        Map<String, Integer> mapaStringsIntegers = new HashMap<>();
        Map<String, Float> mapaStringsFloats = new HashMap<>();

        Set<String> conjuntoStrings = new HashSet<>();
        Set<Integer> conjuntoIntegers = new HashSet<>();
        Set<Float> conjuntoFloats = new HashSet<>();
    }
}
