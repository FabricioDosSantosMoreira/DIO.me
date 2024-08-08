// ├───────> Exercício - Dicionário:
// │             Crie uma classe chamada 'Dicionario' que utilize um Map para armazenar palavras e suas 
// │         respectivas definições. Implemente os seguintes métodos:
// │
// │            * adicionarPalavra(String palavra, String definicao):
// │                  Adiciona uma palavra e sua definição ao dicionário, associando a palavra à sua 
// │                  definição correspondente.
// │
// │            * removerPalavra(String palavra):
// │                  Remove uma palavra do dicionário, dado o termo a ser removido.
// │
// │            * exibirPalavras(): 
// │                  Exibe todas as palavras e suas definições do dicionário, mostrando cada palavra 
// │                  seguida de sua respectiva definição.
// │
// │            * pesquisarPorPalavra(String palavra):
// │                  Pesquisa uma palavra no dicionário e retorna sua definição correspondente.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.map.Basico.Dicionario;

public class Main {

    public static void main(String[] args) {
        
        // Instânciando um objeto da classe 'Dicionario'
        Dicionario dicionario = new Dicionario();

        // Adicionando palavras
        dicionario.adicionarPalavra("Epifania", "Manifestação súbita de uma ideia ou compreensão profunda, geralmente acompanhada por um sentimento de realização.");
        dicionario.adicionarPalavra("Procrastinação", "Ação de adiar ou postergar tarefas ou decisões importantes.");

        // Exibindo as palavras
        dicionario.exibirPalavras();
        
        // Remover uma palavra
        dicionario.removerPalavra("Epifania");

        // Pesquisar uma definição
        String definicao = dicionario.pesquisarPorPalavra("Procrastinação");
        System.out.println("Definição da palavra 'Procrastinação': " + definicao);
    }
}
