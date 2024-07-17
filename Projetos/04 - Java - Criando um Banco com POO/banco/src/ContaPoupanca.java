public class ContaPoupanca extends Conta {

    @Override
    public void imprimirExtrato() {
        System.out.println("\nExtrato Conta Poupança");
        super.exibirInfo();
    }
}
