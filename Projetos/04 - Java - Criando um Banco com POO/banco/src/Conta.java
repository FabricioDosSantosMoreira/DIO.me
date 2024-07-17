import java.sql.Struct;

public abstract class Conta implements IConta {

    // Atributos
    private static final int AGENCIA_PADRAO = 0001;
    private static int SEQUENCIAL = 1;

    protected int agencia;
    protected int numero;
    protected double saldo;

    // Construtor
    public Conta() {
        this.agencia = AGENCIA_PADRAO;
        this.numero = SEQUENCIAL++;
    }


    // Métodos
    @Override
    public void sacar(double valor) {
        System.out.printf("\nSacando %.2f%n", valor);
        this.saldo -= valor;
    }

    @Override
    public void depositar(double valor) {
        System.out.printf("\nDepositando %.2f%n", valor);
        this.saldo += valor;
    }

    @Override
    public void transferir(double valor, Conta contaDestino) {
        System.out.printf("\nTransferindo %.2f%n", valor);
        this.sacar(valor);
        contaDestino.depositar(valor);
    }

    protected void exibirInfo() {
        System.out.println("| Agência: " + this.agencia);
        System.out.println("| Número: " + this.numero);
        System.out.println(String.format("| Saldo: %.2f", this.saldo) + "R$");
    }


    // Getters
    public int getAgencia() {
        return agencia;
    }

    public int getNumero() {
        return numero;
    }

    public double getSaldo() {
        return saldo;
    }
}
