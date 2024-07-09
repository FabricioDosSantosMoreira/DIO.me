// ├───┬───> Exercício: Lista de Tarefa
// │   │
// │   └───>    Crie uma classe chamada "tarefas" que possui uma lista de tarefas como atributo.
// │         Cada tarefa é representada por uma classe chamada "Tarefa" que possui um atributo de descrição.
// │         Implemente os seguintes métodos:
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

        // Instânciando um objeto da classe 'tarefas'
        ListaTarefa tarefas = new ListaTarefa();

        // Adicionando tarefas
        tarefas.adicionarTarefa("Tarefa 1");
        tarefas.adicionarTarefa("Tarefa 2");
        tarefas.adicionarTarefa("Tarefa 3");

        // Exibindo o número total de tarefas
        System.out.println("\nNúmero total de tarefas: " + tarefas.qtdTotalTarefas());

        // Exibindo as descrições das tarefas
        tarefas.exibirDescricoesTarefas();

        // Removendo uma tarefa
        tarefas.removerTarefa("Tarefa 1");

        // Exibindo o número total de tarefas
        System.out.println("\nNúmero total de tarefas: " + tarefas.qtdTotalTarefas());

        // Exibindo as descrições das tarefas
        tarefas.exibirDescricoesTarefas();

        // Removendo tarefas
        tarefas.removerTarefa("Tarefa 2");
        tarefas.removerTarefa("Tarefa 3");

        // Exibindo o número total de tarefas na 'tarefas'
        System.out.println("\nNúmero total de tarefas: " + tarefas.qtdTotalTarefas());

        // Exibindo as descrições das tarefas
        tarefas.exibirDescricoesTarefas();
    }
}
