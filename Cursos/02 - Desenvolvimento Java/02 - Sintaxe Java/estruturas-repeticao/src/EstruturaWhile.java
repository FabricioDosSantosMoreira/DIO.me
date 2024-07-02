import java.util.concurrent.ThreadLocalRandom;
import java.util.Random;

public class EstruturaWhile {
    public static void main(String[] args) {

        // While
        double dinheiro = 50.0;
        while (dinheiro > 0) {

            Double valor = valorAleatorio();

            if(valor > dinheiro) {
                valor = dinheiro;
            }

            System.out.println("Valor: " + valor + " Adicionado ao carrinho");
            dinheiro = dinheiro - valor;
        }

        System.out.println("Dinheiro: " + dinheiro);
        System.out.println("Gastou todo o dinheiro!");


        // Do-While
        System.out.println("Discando...");

        do {
            System.out.println("O telefone está tocando!");
        } while (tocando());

        System.out.println("O telefone foi atendido!");

    }

    private static boolean tocando() {
        boolean atendeu = new Random().nextInt(3) == 1;
        System.out.println("Atendeu? " + atendeu);
        return !atendeu; //negando o ato de continuar tocando
    }


    private static double valorAleatorio() {
        return ThreadLocalRandom.current().nextDouble(2, 10);
    }
}
