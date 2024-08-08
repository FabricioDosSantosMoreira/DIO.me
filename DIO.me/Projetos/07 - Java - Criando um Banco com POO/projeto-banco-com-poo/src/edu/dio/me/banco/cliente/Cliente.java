package edu.dio.me.banco.cliente;

import java.util.ArrayList;

import edu.dio.me.banco.conta.IConta;

public class Cliente {
    
    // Atributos
    private String nome;

    // Construtor
    public Cliente(String nome) {
        this.nome = nome;
    }

    // Métodos 'getters' e 'setters'
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
}
