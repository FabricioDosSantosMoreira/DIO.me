package edu.dio.me;

public class ArgumentosViaTerminal {

    // 1. Compile o arquivo Java: 
    //        javac src/edu/dio/me/ArgumentosViaTerminal.java -d bin/ -verbose    
    //
    // 2. Navegue até o diretório de saída do arquivo Java compilado:
    //        cd bin/
    //
    // 3. Execute o arquivo Java compilado:
    //        java --enable-preview edu.dio.me.ArgumentosViaTerminal Fabrício "dos Santos Moreira" 19 1.85

    public static void main(String[] args) {
         
        System.out.println("\nExecutando o arquivo Java via terminal e com os argumentos:");
        for (String arg : args) {
            System.out.print(arg + " ");
        }

        // Atribuindo os argumentos para variáveis
        String nome = args[0];
        String sobrenome = args[1];
        int idade = Integer.valueOf(args[2]);
        double altura = Double.valueOf(args[3]);
        
        // Exibindo as variáveis 
        System.out.println("\n\nNome: " + nome);
        System.out.println("Sobrenome: " + sobrenome);
        System.out.println("Idade: " + idade);
        System.out.println("Altura: " + altura);
    }   
}
