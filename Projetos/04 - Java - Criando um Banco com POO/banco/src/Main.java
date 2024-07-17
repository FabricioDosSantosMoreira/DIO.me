public class Main {
    public static void main(String[] args) {
        Conta cc = new ContaCorrente();
        Conta cp = new ContaPoupanca();

        cc.depositar(1000);
        cc.transferir(1000, cp);

        cc.imprimirExtrato();

        cp.imprimirExtrato();

    }
}
