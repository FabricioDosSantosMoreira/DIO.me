package optional;

import java.util.Optional;

// Optional
// O objetivo da classe Optional no Java é fornecer uma abordagem mais segura e expressiva para tratar 
// casos em que um valor pode ser ausente (nulo). Ela foi introduzida a partir do Java 8 para evitar o temido 
// NullPointerException (NPE) que é comum quando se trabalha com referências nulas. Optional permite encapsular 
// um valor que pode ser nulo dentro de um objeto Optional. Isso indica explicitamente que o valor pode ou não 
// estar presente e requer que o código que deseja acessá-lo faça uma verificação explícita.


public class OptionalExample {
    
    public static void main(String[] args) {
        
        //of(value): Cria um Optional contendo o valor fornecido. Se o valor for nulo, lançará uma exceção NullPointerException.
        
        Optional<String> optionalValue = Optional.of("Hello");
        System.out.println(optionalValue.get());
        
        //ofNullable(value): Cria um Optional contendo o valor fornecido, mas permite que o valor seja nulo.
        String nullableValue = null;
        Optional<String> optionalValue1 = Optional.ofNullable(nullableValue);
        System.out.println(optionalValue1.isPresent());
        
        //empty(): Retorna um Optional vazio (sem valor).
        Optional<String> optionalValue2 = Optional.empty();
        System.out.println(optionalValue2.isPresent());
        
        //isPresent(): Verifica se o Optional contém um valor não nulo.
        Optional<String> optionalValue3 = Optional.of("Hello");
        System.out.println(optionalValue3.isPresent());
        
        //isEmpty() (A partir do Java 11): Verifica se o Optional está vazio (não contém um valor não nulo).
        Optional<String> optionalValue4 = Optional.ofNullable(null);
        System.out.println(optionalValue4.isEmpty());
        
        //get(): Obtém o valor contido no Optional. Se o valor for nulo, lançará uma exceção NoSuchElementException.
        Optional<String> optionalValue5 = Optional.of("Hello");
        System.out.println(optionalValue5.get());
        
        //orElse(defaultValue): Obtém o valor contido no Optional, ou retorna um valor padrão se o Optional estiver vazio
        Optional<String> optionalValue6 = Optional.ofNullable(null);
        String result = optionalValue6.orElse("Default"); 
        System.out.println(result);
        
        //orElseGet(supplier): Obtém o valor contido no Optional, ou retorna um valor fornecido por um Supplier se o Optional estiver vazio.
        Optional<String> optionalValue7 = Optional.ofNullable(null);
        String result1 = optionalValue7.orElseGet(() -> "Value from Supplier");
        System.out.println(result1);
        
        //orElseThrow(exceptionSupplier): Obtém o valor contido no Optional, ou lança uma exceção fornecida por um Supplier se o Optional estiver vazio.
        //Optional<String> optionalValue8 = Optional.ofNullable(null);
        //String result2 = optionalValue8.orElseThrow(() -> new RuntimeException("Value not present"));
        
        //ifPresent(consumer): Executa uma ação fornecida por um Consumer se o Optional contiver um valor.
        Optional<String> optionalValue9 = Optional.of("Hello");
        optionalValue9.ifPresent(value -> System.out.println("Valor presente: " + value));
    }
}
