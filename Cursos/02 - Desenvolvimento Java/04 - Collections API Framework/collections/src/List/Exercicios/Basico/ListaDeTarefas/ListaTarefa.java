package List.Exercicios.Basico.ListaDeTarefas;

import java.util.ArrayList;
import java.util.List;


public class ListaTarefa {
    
    // Atributo da classe 'ListaTarefa'
    private List<Tarefa> listaTarefas;

    // Construtor da classe 'ListaTarefa'
    public ListaTarefa() {
        this.listaTarefas = new ArrayList<>();
    }

    // Métodos da classe 'ListaTarefa'
    public void adicionarTarefa(String descricao) {
        this.listaTarefas.add(new Tarefa(descricao));
    }

    public void removerTarefa(String descricao) { 
        if (!this.listaTarefas.isEmpty()) {
            List<Tarefa> listaTarefasParaRemover = new ArrayList<>();

            for (Tarefa t : this.listaTarefas) {
                if (t.getDescricao().equalsIgnoreCase(descricao))  {
                    listaTarefasParaRemover.add(t);
                }
            }

            this.listaTarefas.removeAll(listaTarefasParaRemover);
        } else {
            System.out.println("\nA lista está vazia!");
        }
    }

    public int qtdTotalTarefas() {
        return this.listaTarefas.size();
    }

    public void exibirDescricoesTarefas() {
        if (!this.listaTarefas.isEmpty()) {
            System.out.println("\n| Lista de tarefas: ");
            for (Tarefa t : this.listaTarefas) {
                System.out.println("| Tarefa: " + t.getDescricao());
            }
        } else {
            System.out.println("\nA lista está vazia!");
        }
    }
}
