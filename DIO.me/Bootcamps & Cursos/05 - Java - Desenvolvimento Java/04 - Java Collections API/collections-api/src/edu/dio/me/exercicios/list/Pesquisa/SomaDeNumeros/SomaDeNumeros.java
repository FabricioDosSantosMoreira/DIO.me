package edu.dio.me.exercicios.list.Pesquisa.SomaDeNumeros;

import java.util.ArrayList;
import java.util.List;


public class SomaDeNumeros {

    // Atributo da classe 'SomaDeNumeros'
    List<Integer> listaNumeros;

    // Método construtor da classe 'SomaDeNumeros'
    public SomaDeNumeros() {
        this.listaNumeros = new ArrayList<>();
    } 

    // Métodos da classe 'SomaDeNumeros'
    public void adicionarNumero(int numero) {
        this.listaNumeros.add(numero);
    }

    public int calcularSoma() {
        int soma = 0;
        
        for (Integer numero : listaNumeros) {
            soma += numero;
        }
        return soma;
    }

    public int encontrarMaiorNumero() {
        int maiorNumero = Integer.MIN_VALUE;

        if(!this.listaNumeros.isEmpty()) {
            for (Integer numero : this.listaNumeros) {
                if (numero >= maiorNumero) {
                    maiorNumero = numero;
                }
            }
        } else {
            System.out.println("\nA lista de números está vazia!");
        }
        return maiorNumero;
    }

    public int encontrarMenorNumero() {
        int menorNumero = Integer.MAX_VALUE;

        if(!this.listaNumeros.isEmpty()) {
            for (Integer numero : this.listaNumeros) {
                if (numero <= menorNumero) {
                    menorNumero = numero;
                }
            }
        } else {
            System.out.println("\nA lista de números está vazia!");
        }
        return menorNumero;
    }

    public void exibirNumeros() {   
        if(!this.listaNumeros.isEmpty()) {
            System.out.println("\n| Lista de números: " + this.listaNumeros);
        } else {
            System.out.println("\nA lista de números está vazia!");
        }
    }
}
