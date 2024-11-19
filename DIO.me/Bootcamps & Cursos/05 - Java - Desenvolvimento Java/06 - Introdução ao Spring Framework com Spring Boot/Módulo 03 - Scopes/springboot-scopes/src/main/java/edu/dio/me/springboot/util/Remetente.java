package edu.dio.me.springboot.util;

public class Remetente {

    // Atributos da Classe 'Remetente'
    private String nome;
    private String email;

    // Método 'toString' da classe 'Remetente'
    @Override
    public String toString() {
        return "Remetente [nome=" + nome + ", email=" + email + "]";
    }

    // Métdos 'getters' e 'setters'
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
