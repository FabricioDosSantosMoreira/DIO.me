package edu.me.sintaxe;

public class Operadores {
    public static void main(String[] args) {


        // Operadores aritméticos
        int a = 10, b = 5;
        int soma = a + b; // Operador de adição
        int subtracao = a - b; // Operador de subtração
        int multiplicacao = a * b; // Operador de multiplicação
        int divisao = a / b; // Operador de divisão
        int resto = a % b; // Operador de módulo (resto da divisão)

        // Operadores de incremento e decremento
        int numero = 15;
        numero++; // Incremento 
        numero--; // Decremento
        -- numero;
        ++ numero; // Incremento antes

        // Operadores de atribuição
        int x = 10;
        x += 5; // Equivalente a x =  x + 5;
        x -= 3; // Equivalente a x = x - 3;
        x *= 2; // Equivalente a x = x * 2;
        x /= 4; // Equivalente a x = x / 4;
        x %= 3; // Equivalente a x = x % 3;

        // Operadores de comparação
        int p = 5, q = 10;
        boolean igual = (p == q); // Igualdade
        boolean diferente = (p != q); // Diferença
        boolean maiorQue = (p > q); // Maior que
        boolean menorQue = (p < q); // Menor que
        boolean maiorOuIgual = (p >= q); // Maior ou igual a
        boolean menorOuIgual = (p <= q); // Menor ou igual a

        // Operadores lógicos
        boolean condicao1 = true, condicao2 = false;
        boolean eLogico = condicao1 && condicao2; // AND lógico
        boolean ouLogico = condicao1 || condicao2; // OR lógico
        boolean naoLogico = !condicao1; // NOT lógico

        // Operadores bit a bit (para inteiros)
        int m = 5, n = 3;
        int andBitwise = m & n; // AND bit a bit
        int orBitwise = m | n; // OR bit a bit
        int xorBitwise = m ^ n; // XOR bit a bit
        int complementoBitwise = ~m; // Complemento bit a bit
        int deslocamentoEsquerda = m << 1; // Deslocamento de bits para a esquerda
        int deslocamentoDireita = m >> 1; // Deslocamento de bits para a direita

        // Operador condicional (ternário)
        int idade = 20;
        String status = (idade >= 18) ? "Adulto" : "Menor de idade";

        // Operador de concatenação (para strings)
        String nome = "João";
        String sobrenome = "Silva";
        String nomeCompleto = nome + " " + sobrenome;

        // Impressão dos resultados
        System.out.println("Operadores em Java:");
        System.out.println("Soma: " + soma);
        System.out.println("Subtração: " + subtracao);
        System.out.println("Multiplicação: " + multiplicacao);
        System.out.println("Divisão: " + divisao);
        System.out.println("Resto: " + resto);
        System.out.println("Incremento: " + numero);
        System.out.println("Decremento: " + numero);
        System.out.println("Atribuição: " + x);
        System.out.println("Comparação - Igual: " + igual);
        System.out.println("Comparação - Diferente: " + diferente);
        System.out.println("Comparação - Maior que: " + maiorQue);
        System.out.println("Comparação - Menor que: " + menorQue);
        System.out.println("Comparação - Maior ou igual: " + maiorOuIgual);
        System.out.println("Comparação - Menor ou igual: " + menorOuIgual);
        System.out.println("AND lógico: " + eLogico);
        System.out.println("OR lógico: " + ouLogico);
        System.out.println("NOT lógico: " + naoLogico);
        System.out.println("AND bit a bit: " + andBitwise);
        System.out.println("OR bit a bit: " + orBitwise);
        System.out.println("XOR bit a bit: " + xorBitwise);
        System.out.println("Complemento bit a bit: " + complementoBitwise);
        System.out.println("Deslocamento para a esquerda: " + deslocamentoEsquerda);
        System.out.println("Deslocamento para a direita: " + deslocamentoDireita);
        System.out.println("Operador condicional: " + status);
        System.out.println("Concatenação de strings: " + nomeCompleto);
    }
}
