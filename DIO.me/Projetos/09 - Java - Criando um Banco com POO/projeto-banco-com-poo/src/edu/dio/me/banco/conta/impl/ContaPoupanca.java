package edu.dio.me.banco.conta.impl;

import edu.dio.me.banco.cliente.Cliente;

public class ContaPoupanca extends Conta {

    public ContaPoupanca(double saldo, Cliente cliente) {
        super(saldo, cliente);
    }

    @Override
    public void imprimirExtrato() {
        System.out.println("\nExtrato Conta Poupança");
        super.exibirInfo();
    }
}
