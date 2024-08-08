package edu.dio.me.banco.conta.impl;

import edu.dio.me.banco.cliente.Cliente;

public class ContaCorrente extends Conta {

    public ContaCorrente(double saldo, Cliente cliente) {
        super(saldo, cliente);
    }

    @Override
    public void imprimirExtrato() {
        System.out.println("\nExtrato Conta Corrente");
        super.exibirInfo();
    }
}
