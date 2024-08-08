// ├───────> Exercício - Lista de Tarefas:
// │             Crie uma classe chamada 'ListaTarefas' que possui um conjunto de objetos do 
// │         tipo 'Tarefa' como atributo. Cada tarefa possui um atributo de descrição e um 
// │         atributo booleano para indicar se a tarefa foi concluída ou não. 
// │         Implemente os seguintes métodos:
// │
// │             * adicionarTarefa(String descricao):
// │                   Adiciona uma nova tarefa ao Set.
// │
// │             * removerTarefa(String descricao):
// │                   Remove uma tarefa do Set de acordo com a descrição, se estiver presente.
// │
// │             * exibirTarefas():
// │                   Exibe todas as tarefas da lista de tarefas.
// │
// │             * contarTarefas():
// │                   Conta o número total de tarefas na lista de tarefas.
// │
// │             * obterTarefasConcluidas():
// │                   Remove uma tarefa do Set de acordo com a descrição, se estiver presente.
// │
// │             * obterTarefasPendentes():
// │                   Exibe todas as tarefas da lista de tarefas.
// │
// │             * marcarTarefaConcluida(String descricao):
// │                    Marca uma tarefa como concluída de acordo com a descrição.
// │  
// │             * marcarTarefaPendente(String descricao):
// │                   Marca uma tarefa como pendente de acordo com a descrição.
// │
// │             * limparListaTarefas(): 
// │                   Remove todas as tarefas da lista de tarefas.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.set.Pesquisa.ListaDeTarefas;

public class Main {

    public static void main(String[] args) {
        
        // Instânciando um objeto da classe 'tarefas'
        ListaTarefa tarefas = new ListaTarefa();

        // Adicionando tarefas
        tarefas.adicionarTarefa("Tarefa 1");
        tarefas.adicionarTarefa("Tarefa 2");
        tarefas.adicionarTarefa("Tarefa 3");
        tarefas.adicionarTarefa("Tarefa 4");

        tarefas.removerTarefa("Tarefa 4");

        tarefas.marcarTarefaConcluida("Tarefa 1");
        tarefas.marcarTarefaConcluida("Tarefa 2");
        tarefas.marcarTarefaPendente("Tarefa 3");

        tarefas.exibirTarefas();

        tarefas.contarTarefas();

        tarefas.limparListaTarefas();
    }
}
