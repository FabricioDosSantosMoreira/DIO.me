// ├───┬───> Exercício: Lista de Tarefa
// │   │
// │   └───>    Crie uma classe chamada "ListaTarefa" que possui uma lista de tarefas como atributo.
// │        Cada tarefa é representada por uma classe chamada "Tarefa" que possui um atributo de descrição.
// │        Implemente os seguintes métodos:
// │
// │            * adicionarTarefa(String descricao): Adiciona uma nova tarefa à lista com a descrição fornecida.
// │            * removerTarefa(String descricao): Remove uma tarefa da lista com base em sua descrição.
// │            * qtdTotalTarefas(): Retorna o número total de tarefas na lista.
// │            * exibirDescricoesTarefas(): Exibe a descrição de todas as tarefas na lista.
// │
// │
// │
// └───────> Código:

package List.Exercicios.Basico.ListaDeTarefas;

public class Main {
    public static void main(String[] args) {

        // Instânciando um objeto da classe 'ListaTarefa'
        ListaTarefa listaTarefa = new ListaTarefa();

        // Adicionando tarefas à 'listaTarefa'
        listaTarefa.adicionarTarefa("Tarefa 1");
        listaTarefa.adicionarTarefa("Tarefa 2");
        listaTarefa.adicionarTarefa("Tarefa 3");

        // Exibindo o número total de tarefas na 'listaTarefa'
        System.out.println("\nNúmero total de tarefas: " + listaTarefa.qtdTotalTarefas());

        // Exibindo as descrições de tarefas na 'listaTarefa'
        listaTarefa.exibirDescricoesTarefas();

        // Removendo uma tarefa da 'listaTarefa'
        listaTarefa.removerTarefa("Tarefa 1");

        // Exibindo as descrições de tarefas na 'listaTarefa'
        listaTarefa.exibirDescricoesTarefas();

        // Exibindo o número total de tarefas na 'listaTarefa'
        System.out.println("\nNúmero total de tarefas: " + listaTarefa.qtdTotalTarefas());

        // Removendo tarefas da 'listaTarefa'
        listaTarefa.removerTarefa("Tarefa 2");
        listaTarefa.removerTarefa("Tarefa 3");

        // Exibindo o número total de tarefas na 'listaTarefa'
        System.out.println("\nNúmero total de tarefas: " + listaTarefa.qtdTotalTarefas());
    }
}
