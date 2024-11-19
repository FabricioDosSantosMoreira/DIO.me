// ├───────> Exercício - Contagem de Palavras:
// │             Crie uma classe chamada 'ContagemPalavras' que utilize um Map para armazenar as 
// │         palavras e a quantidade de vezes que cada palavra aparece em um texto. 
// │         Implemente os seguintes métodos:
// │
// │             * adicionarPalavra(String palavra, Integer contagem):
// │                   Adiciona uma palavra à contagem.
// │
// │             * removerPalavra(String palavra): 
// │                   Remove uma palavra da contagem, se estiver presente.
// │
// │             * exibirContagemPalavras():
// │                   Exibe todas as palavras e suas respectivas contagens.
// │
// │             * encontrarPalavraMaisFrequente(): 
// │                   Encontra a palavra mais frequente no texto e retorna a palavra.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.map.Pesquisa.ContagemDePalavras;

public class Main {

    public static void main(String[] args) {
        
        // Instânciando um objeto da classe 'ContagemDePalavras'
        ContagemDePalavras palavras = new ContagemDePalavras();

        // Adiciona palavras e suas contagens
        palavras.adicionarPalavra("Java", 2);
        palavras.adicionarPalavra("Python", 8);
        palavras.adicionarPalavra("JavaScript", 1);
        palavras.adicionarPalavra("C#", 6);

        palavras.removerPalavra("C#");
       
        // Exibe a contagem total de palavras
        palavras.exibirContagemPalavras();

        // Encontra e exibe a palavra mais frequente
        String palavraMaisFrequente = palavras.encontrarPalavraMaisFrequente();
        System.out.println("A palavra mais frequente é: " + palavraMaisFrequente);
        }
}
