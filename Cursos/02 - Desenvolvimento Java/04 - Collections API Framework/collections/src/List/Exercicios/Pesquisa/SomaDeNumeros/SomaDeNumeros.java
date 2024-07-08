package List.Exercicios.Pesquisa.SomaDeNumeros;

import java.util.ArrayList;
import java.util.List;


public class SomaDeNumeros {

    List<Integer> numeros;

    public SomaDeNumeros() {
        this.numeros = new ArrayList<>();
    } 

    public void adicionarNumero(int numero) {
        this.numeros.add(numero);
    }

    public int calcularSoma() {
        int soma = 0;
        
        for (Integer numero : numeros) {
            soma += numero;
        }

        return soma;
    }

    public int encontrarMaiorNumero() {
        int maiorNumero = Integer.MIN_VALUE;

        if(!this.numeros.isEmpty()) {
            for (Integer numero : this.numeros) {
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

        if(!this.numeros.isEmpty()) {
            for (Integer numero : this.numeros) {
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

        if(!this.numeros.isEmpty()) {
            System.out.println("\n| Lista de números: " + this.numeros);
        } else {
            System.out.println("\nA lista de números está vazia!");
        }
    }
}
