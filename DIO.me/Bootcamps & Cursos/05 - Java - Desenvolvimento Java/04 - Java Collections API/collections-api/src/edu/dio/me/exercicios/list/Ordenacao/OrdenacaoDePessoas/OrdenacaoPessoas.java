package edu.dio.me.exercicios.list.Ordenacao.OrdenacaoDePessoas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class OrdenacaoPessoas {

    // Atributo da classe 'OrdenacaoPessoas'
    private List<Pessoa> pessoas;
    
    // Método construtor da classe 'OrdenacaoPessoas'
    public OrdenacaoPessoas() {
        this.pessoas = new ArrayList<>();
    }

    // Métodos da classe 'OrdenacaoPessoas'
    public void adicionarPessoa(String nome, int idade, double altura) {
        this.pessoas.add(new Pessoa(nome, idade, altura));
    }

    public List<Pessoa> ordenarPorIdade() {
        List<Pessoa> pessoasPorIdade = new ArrayList<>(this.pessoas);

        if (!this.pessoas.isEmpty()) {
            Collections.sort(pessoasPorIdade);
        } else {
            System.out.println("A lista está vazia!");
        }
        return pessoasPorIdade;
    }

    public List<Pessoa> ordenarPorAltura() {
        List<Pessoa> pessoasPorAltura = new ArrayList<>(this.pessoas);

        if (!this.pessoas.isEmpty()) {
            Collections.sort(pessoasPorAltura, new CompararAlturaPessoa());
        } else {
            System.out.println("A lista está vazia!");
        }
        return pessoasPorAltura;
    }

    public List<Pessoa> getPessoas() {
        return pessoas;
    }
}


class CompararAlturaPessoa implements Comparator<Pessoa> {
    @Override
    public int compare(Pessoa p1, Pessoa p2) {
        return Double.compare(p1.getAltura(), p2.getAltura());
    }
}
