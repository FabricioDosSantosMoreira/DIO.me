package edu.dio.me.exercicios.list.Ordenacao.OrdenacaoDeNumeros;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class OrdenacaoNumeros {
    
    // Atributo da classe 'OrdenacaoNumeros'
    private List<Integer> listaNumeros;

    // Método construtor da classe 'OrdenacaoNumeros'
    public OrdenacaoNumeros() {
        this.listaNumeros = new ArrayList<>();
    }

    // Métodos da classe 'OrdenacaoNumeros'
    public void adicionarNumero(int numero) {
        this.listaNumeros.add(numero);
    }

    public List<Integer> ordenarCrescente() {
        List<Integer> numerosCrescente = new ArrayList<>(this.listaNumeros);

        if (!this.listaNumeros.isEmpty()) {
            Collections.sort(numerosCrescente);
        } else {
            System.out.println("\nA lista de números está vazia!");
        }
        return numerosCrescente;
    }

    public List<Integer> ordenarDecrescente() {
        List<Integer> numerosDecrescente = new ArrayList<>(this.listaNumeros);

        if (!this.listaNumeros.isEmpty()) {
            numerosDecrescente.sort(Collections.reverseOrder());
        } else {
            System.out.println("\nA lista de números está vazia!");
        }
        return numerosDecrescente;
    }

    public void exibirNumeros() {
        if (!this.listaNumeros.isEmpty()) {
          System.out.println(this.listaNumeros.toString());
        } else {
            System.out.println("\nA lista de números está vazia!");
        }
    }
}