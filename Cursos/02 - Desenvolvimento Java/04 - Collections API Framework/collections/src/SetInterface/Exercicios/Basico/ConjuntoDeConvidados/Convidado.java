package SetInterface.Exercicios.Basico.ConjuntoDeConvidados;

import java.util.Objects;

public class Convidado {

    // Atributos da classe 'Convidado'
    private String nome;
    private int codigoConvite;
    
    // Construtor da classe 'Convidado'
    public Convidado(String nome, int codigoConvite) {
        this.nome = nome;
        this.codigoConvite = codigoConvite;
    }

    // Método 'toString' da classe 'Convidado'
    @Override
    public String toString() {
        return "Convidado [nome=" + nome + ", codigoConvite=" + codigoConvite + "]";
    }

    // Método 'hashCode' da classe 'Convidado'
    @Override
    public int hashCode() {
        return Objects.hash(getCodigoConvite());
    }

    // Método 'equals' da classe 'Convidado'
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Convidado convidado)) return false;
        return getCodigoConvite() == convidado.getCodigoConvite();
    }
    
    // Getters e Setter da classe 'Convidado'
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getCodigoConvite() {
        return codigoConvite;
    }

    public void setCodigoConvite(int codigoConvite) {
        this.codigoConvite = codigoConvite;
    }
}
