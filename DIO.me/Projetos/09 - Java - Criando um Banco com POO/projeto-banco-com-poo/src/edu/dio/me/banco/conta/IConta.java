package edu.dio.me.banco.conta;

import edu.dio.me.banco.conta.impl.Conta;

public interface IConta {

    void sacar(double valor);
    
    void depositar(double valor);

    void transferir(double valor, Conta contaDestino);

    void imprimirExtrato();
}
