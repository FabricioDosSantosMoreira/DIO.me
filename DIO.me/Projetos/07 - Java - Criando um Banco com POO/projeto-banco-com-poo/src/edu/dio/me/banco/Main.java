package edu.dio.me.banco;

import edu.dio.me.banco.cliente.Cliente;
import edu.dio.me.banco.conta.impl.Conta;
import edu.dio.me.banco.conta.impl.ContaCorrente;
import edu.dio.me.banco.conta.impl.ContaPoupanca;

public class Main {
    public static void main(String[] args) {

        Cliente cliente_a = new Cliente("Cliente A");
        Cliente cliente_b = new Cliente("Cliente B");

        Conta cc_cliente_a = new ContaCorrente(1000, cliente_a);
        Conta cp_cliente_a = new ContaPoupanca(1500, cliente_a);

        Conta cc_cliente_b = new ContaCorrente(2000, cliente_b);

        cc_cliente_a.imprimirExtrato();

        cc_cliente_a.depositar(1000);

        cc_cliente_a.imprimirExtrato();

        cc_cliente_b.transferir(2000, cc_cliente_a);

        cc_cliente_a.imprimirExtrato();

        cc_cliente_b.imprimirExtrato();
    }
}
