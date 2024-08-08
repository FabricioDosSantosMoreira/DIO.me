package edu.dio.me.exercicios.set.Pesquisa.AgendaDeContatos;

import java.util.HashSet;
import java.util.Set;

public class AgendaContatos {

    // Atributo da classe 'AgendaContatos'
    private Set<Contato> agenda;

    // Método construtor da classe 'AgendaContatos'
    public AgendaContatos() {
        this.agenda = new HashSet<>();
    }

    // Métodos da classe 'AgendaContatos'
    public void adicionarContato(String nome, int numero) {
        this.agenda.add(new Contato(nome, numero));
    }

    public void exibirContatos() {
        if(!this.agenda.isEmpty()) {
            System.out.print("\nAgenda de contatos = ");
            System.out.println(this.agenda);
        } else {
            System.out.println("\nA agenda de contatos está vazia!");
        }
    }

    public Set<Contato> pesquisarPorNome(String nome) {
        Set<Contato> contatosPorNome = new HashSet<>();

        if(!this.agenda.isEmpty()) { 
            for(Contato c : this.agenda) {
                if(c.getNome().startsWith(nome)) {
                    contatosPorNome.add(c);
                } 
            }
        } else {
            System.out.println("\nA agenda de contatos está vazia!");
        }
        return contatosPorNome;
    }

    public Contato atualizarNumeroContato(String nome, int novoNumero) {
        Contato contatoAtualizado = null;

        if(!this.agenda.isEmpty()) {

            for(Contato c : this.agenda) {
                if(c.getNome().equalsIgnoreCase(nome)) {
                    c.setNumero(novoNumero);
                    contatoAtualizado = c;
                } 
            } 
        } else {
            System.out.println("\nA agenda de contatos está vazia!");
        }
        return contatoAtualizado;
    }
}
