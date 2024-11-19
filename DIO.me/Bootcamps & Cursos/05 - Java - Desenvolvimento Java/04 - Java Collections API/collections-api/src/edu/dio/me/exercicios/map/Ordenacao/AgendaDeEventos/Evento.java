package edu.dio.me.exercicios.map.Ordenacao.AgendaDeEventos;

public class Evento {

    // Atributos da classe 'Evento'
    private String nome;
    private String atracao;

    // Método construtor da classe 'Evento'
    public Evento(String nome, String atracao) {
        this.nome = nome;
        this.atracao = atracao;
    }

    // Método 'toString()' da classe 'Evento'
    @Override
    public String toString() {
        return "Evento [nome=" + nome + ", atracao=" + atracao + "]";
    }

    // Métodos 'getters' e 'setters' da classe 'Evento'
    public String getNome() {
        return nome;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getAtracao() {
        return atracao;
    }

    public void setAtracao(String atracao) {
        this.atracao = atracao;
    } 
}
