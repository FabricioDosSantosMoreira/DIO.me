package edu.dio.me.exercicios.set.Basico.ConjuntoDeConvidados;

import java.util.HashSet;
import java.util.Set;

public class ConjuntoConvidados {

    // Atributo da classe 'ConjuntoConvidados'
    private Set<Convidado> setConvidados;

    // Construtor da classe 'ConjuntoConvidados'
    public ConjuntoConvidados() {
        this.setConvidados = new HashSet<>();
    }

    // Métodos da classe 'ConjuntoConvidados'
    public void adicionarConvidado(String nome, int codigoConvite) {
        this.setConvidados.add(new Convidado(nome, codigoConvite));
    }

    public void removerConvidadoPorCodigoConvite(int codigoConvite) {
        Convidado convidadoParaRemover = null;

        for(Convidado c : this.setConvidados) {
            if(c.getCodigoConvite() == codigoConvite) {
                convidadoParaRemover = c;
                break;
            } else {
                System.out.println("\nNão existe um convidado com este código de convite!");
            }
        }
        this.setConvidados.remove(convidadoParaRemover);
    }

    public int contarConvidados() {
        return setConvidados.size();
    }

    public void exibirConvidados() {
        if(!this.setConvidados.isEmpty()) {
            System.out.print("\nConjunto de convidados = ");
            System.out.println(this.setConvidados);
        } else {
            System.out.println("\nO conjunto de convidados está vazio!");
        }
    }
}
