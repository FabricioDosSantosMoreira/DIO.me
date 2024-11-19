package edu.dio.me.exercicios.set.Pesquisa.ListaDeTarefas;

import java.util.Set;
import java.util.HashSet;

public class ListaTarefa {

    // Atributo da classe 'ListaTarefa'
    private Set<Tarefa> tarefas;

    // Método construtor da classe 'ListaTarefa'
    public ListaTarefa() {
        this.tarefas = new HashSet<>();
    }

    // Métodos da classe 'ListaTarefa'
    public void adicionarTarefa(String descricao) {
        this.tarefas.add(new Tarefa(descricao));
    }

    public void removerTarefa(String descricao) { 
        if (!this.tarefas.isEmpty()) {
            for (Tarefa t : this.tarefas) {
                if (t.getDescricao().equalsIgnoreCase(descricao))  {
                    this.tarefas.remove(t);
                    System.out.println("\nTarefa removida!");
                    break;
                }
            }
        } else {
            System.out.println("\nNenhuma tarefa!");
        }
    }

    public void exibirTarefas() {
        if (!this.tarefas.isEmpty()) {

            for (Tarefa t : this.tarefas) {
                System.out.println("| Tarefa: " + t);  
            }
        } else {
            System.out.println("\nNenhuma tarefa!");
        }
    }

    public void contarTarefas() {
        if (!this.tarefas.isEmpty()) {
            int coontagem = this.tarefas.size();
            System.out.println("\nContagem de Tarefas: " + coontagem);  
        } else {
            System.out.println("\nNenhuma tarefa!");
        }
    }

    public Set<Tarefa> obterTarefasConcluidas() {
        Set<Tarefa> tarefasConcluidas = new HashSet<>();

        if (!this.tarefas.isEmpty()) {
            for (Tarefa t : this.tarefas) {
                if (t.isConcluida()) {
                    tarefasConcluidas.add(t);
                }
            }
        } else {
            System.out.println("\nNenhuma tarefa!");
        }
        return tarefasConcluidas;
    }

    public Set<Tarefa> obterTarefasPendentes() {
        Set<Tarefa> tarefasPendentes = new HashSet<>();

        if (!this.tarefas.isEmpty()) {
            for (Tarefa t : this.tarefas) {
                if (!t.isConcluida()) {
                    tarefasPendentes.add(t);
                }
            }
        } else {
            System.out.println("\nNenhuma tarefa!");
        }
        return tarefasPendentes;
    }

    public void marcarTarefaConcluida(String descricao) {
        if (!this.tarefas.isEmpty()) {
            for (Tarefa t : this.tarefas) {
                if (t.getDescricao().equalsIgnoreCase(descricao)) {
                    t.setConcluida(true);
                    System.out.println("\nTarefa marcada como concluida!");
                }
            }
        } else {
            System.out.println("\nNenhuma tarefa!");
        }
    }

    public void marcarTarefaPendente(String descricao) {
        if (!this.tarefas.isEmpty()) {
            for (Tarefa t : this.tarefas) {
                if (t.getDescricao().equalsIgnoreCase(descricao)) {
                    t.setConcluida(false);
                    System.out.println("\nTarefa marcada como pendente!");
                }
            }
        } else {
            System.out.println("\nNenhuma tarefa!");
        }
    }

    public void limparListaTarefas() {
        if (!this.tarefas.isEmpty()) {
            this.tarefas.clear();
        } else {
            System.out.println("\nNenhuma tarefa!");
        }
    }
}
