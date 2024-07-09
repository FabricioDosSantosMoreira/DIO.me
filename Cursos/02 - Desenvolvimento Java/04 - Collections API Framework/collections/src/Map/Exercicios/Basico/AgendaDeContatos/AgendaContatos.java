package Map.Exercicios.Basico.AgendaDeContatos;

import java.util.HashMap;
import java.util.Map;


public class AgendaContatos {

    // Atributos da classe 'AgendaContatos'
    private Map<String, Integer> agenda;

    // Construtor da classe 'AgendaContatos'
    public AgendaContatos() {
        this.agenda = new HashMap<>();
    }

    // Métodos da classe 'AgendaContatos'
    public void adicionarContato(String nome, Integer telefone) {
        this.agenda.put(nome, telefone);
    }

    public void removerContato(String nome) {
        if(!this.agenda.isEmpty()) {
            this.agenda.remove(nome);
        } else {
            System.out.println("\nA agenda de contatos está vazia!");
        }
    }

    public void exibirContatos() {
        System.out.println(this.agenda);
    }

    public Integer pesquisarPorNome(String nome) {
        Integer telefonePorNome = null;

        if(!this.agenda.isEmpty()) {
            telefonePorNome = this.agenda.get(nome);
        } else {
            System.out.println("\nA agenda de contatos está vazia!");
        }
        return telefonePorNome;
    }

    // Getters e Setters da classe 'AgendaContatos'
    public Map<String, Integer> getAgenda() {
        return agenda;
    }

    public void setAgenda(Map<String, Integer> agenda) {
        this.agenda = agenda;
    }
}
