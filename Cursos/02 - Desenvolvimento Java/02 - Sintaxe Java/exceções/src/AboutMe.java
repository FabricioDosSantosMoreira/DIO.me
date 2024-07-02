import java.util.Locale;
import java.util.Scanner;

public class AboutMe {
    public static void main(String[] args) {
        //criando o objeto scanner
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);
        
        String nome = "";
        String sobrenome = "";
        int idade = 0;
        double altura = 0.0;

        try {
            System.out.println("Digite seu nome");
            nome = scanner.next();
            
            System.out.println("Digite seu sobrenome");
            sobrenome = scanner.next();

            System.out.println("Digite sua idade");
            idade = scanner.nextInt();
            
            System.out.println("Digite sua altura");
            altura = scanner.nextDouble();

            //imprimindo os dados obtidos pelo usuario
            System.out.println("Ola, me chamo " + nome.toUpperCase() + " " + sobrenome.toUpperCase());
            System.out.println("Tenho " + idade + " anos ");
            System.out.println("Minha altura é " + altura + "cm ");

        } catch(Exception e) {
            System.out.println("Ocorreu uma exceção: " + e);

        } finally {
            scanner.close();  
        }
    }
}