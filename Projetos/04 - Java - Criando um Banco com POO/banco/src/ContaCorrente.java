public class ContaCorrente extends Conta {

    @Override
    public void imprimirExtrato() {
        System.out.println("\nExtrato Conta Corrente");
        super.exibirInfo();
    }
}
