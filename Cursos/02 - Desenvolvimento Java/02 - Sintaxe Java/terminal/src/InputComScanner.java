import java.util.Scanner;
import java.util.Locale;


public class InputComScanner {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);

        System.out.print("\nDigite seu nome: ");
        String nome = scanner.next();

        System.out.println("\nDigite a sua idade: ");
        int idade = scanner.nextInt();


        System.out.println(nome);
        System.out.println(idade);
        
    }
}