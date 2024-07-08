package List.Exercicios.Basico.ListaDeTarefas;

import java.util.ArrayList;
import java.util.List;


public class ListaTarefa {

    private List<Tarefa> tarefas;

    public ListaTarefa() {
        this.tarefas = new ArrayList<>();
    }

    public void adicionarTarefa(String descricao) {
        this.tarefas.add(new Tarefa(descricao));
    }

    public void removerTarefa(String descricao) { 
        if (!this.tarefas.isEmpty()) {
            List<Tarefa> tarefasParaRemover = new ArrayList<>();

            for (Tarefa t : this.tarefas) {
                if (t.getDescricao().equalsIgnoreCase(descricao))  {
                    tarefasParaRemover.add(t);
                }
            }

            this.tarefas.removeAll(tarefasParaRemover);

        } else {
            System.out.println("\nA lista está vazia!");
        }
    }

    public int qtdTotalTarefas() {
        return this.tarefas.size();
    }

    public void exibirDescricoesTarefas() {
        if (!this.tarefas.isEmpty()) {
            System.out.println("\n| Lista de tarefas: ");
            for (Tarefa t : this.tarefas) {
                System.out.println("| Tarefa: " + t.getDescricao());
            }
        } else {
            System.out.println("\nA lista está vazia!");
        }
    }
}
