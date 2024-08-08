// ├───────> Exercício - Conjunto de Palavras Únicas:
// │             Crie uma classe chamada 'ConjuntoPalavrasUnicas' que possui um conjunto de palavras 
// │         únicas como atributo. Implemente os seguintes métodos:
// │
// │             * adicionarPalavra(String palavra): 
// │                   Adiciona uma palavra ao conjunto.
// │
// │             * removerPalavra(String palavra):
// │                   Remove uma palavra do conjunto.
// │
// │             * verificarPalavra(String palavra): 
// │                   Verifica se uma palavra está presente no conjunto.
// │
// │             * exibirPalavrasUnicas():
// │                   Exibe todas as palavras únicas do conjunto.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.set.Basico.ConjuntoDePalavrasUnicas;

public class Main {

    public static void main(String[] args) {
        
        // Instânciando um objeto da classe 'ConjuntoPalavrasUnicas'
        ConjuntoPalavrasUnicas palavras = new ConjuntoPalavrasUnicas();

        // Adicionando palavras únicas
        palavras.adicionarPalavra("Java");
        palavras.adicionarPalavra("Python");
        palavras.adicionarPalavra("JavaScript");
        palavras.adicionarPalavra("Python");
        palavras.adicionarPalavra("C++");
        palavras.adicionarPalavra("Ruby");

        palavras.removerPalavra("C++");

        palavras.verificarPalavra("Python");

        palavras.exibirPalavrasUnicas();

        palavras.verificarPalavra("C++");
    }
}
