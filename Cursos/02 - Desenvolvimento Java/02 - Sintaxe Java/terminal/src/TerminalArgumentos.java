public class TerminalArgumentos {

    public static void main(String[] args) {

        String nome = args[0];
        String sobrenome = args[1];
        int idade = Integer.valueOf(args[2]);
        double altura = Double.valueOf(args[3]);

        System.out.println("\nMeu nome é: " + nome + " " + sobrenome);
        System.out.println("Tenho " + idade + " anos");
        System.out.println("Minha altura é: " + altura + "cm");

        // cd bin
    }   //java --enable-preview TerminalArgumentos Fabrício "dos Santos Moreira" 19 1.85
        // ver launch.json





    
}
