package edu.dio.me.banco.conta.impl;

import edu.dio.me.banco.cliente.Cliente;
import edu.dio.me.banco.conta.IConta;

public abstract class Conta implements IConta {

    // Atributos
    private static final int AGENCIA_PADRAO = 0001;
    private static int SEQUENCIAL = 1;

    protected Cliente cliente;
    protected int agencia;
    protected int numero;
    private double saldo;

    // Construtor
    public Conta(double saldo, Cliente cliente) {
        this.agencia = AGENCIA_PADRAO;
        this.numero = SEQUENCIAL++;

        this.saldo = saldo;
        this.cliente = cliente;
    }

    // Métodos
    @Override
    public void sacar(double valor) {
        System.out.printf("\nSacando %.2f%n", valor);

        if (this.saldo >= valor) {
            this.saldo -= valor;
            System.out.println("Sucesso. Saque realizado!");
        } else {
            System.out.println("Erro. O saldo é insuficiente!");
        }
        
    }

    @Override
    public void depositar(double valor) {
        System.out.printf("\nDepositando %.2f%n", valor);

        if (valor > 0) {
            this.saldo += valor;
            System.out.println("Sucesso. Depósito realizado!");
        } else {
            System.out.println("Erro. O valor é inválido!");
        }
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

    // Métodos 'getters'
    public int getAgencia() {
        return agencia;
    }

    public int getNumero() {
        return numero;
    }
}
