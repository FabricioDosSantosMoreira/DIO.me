package edu.dio.me.springboot.util;

public class ViaCepResponse {

    // Atributos da classe 'ViaCepResponse'
    private String cep;
    private String logradouro;
    private String localidade;

    // Método 'toString' da classe 'ViaCepResponse'
    @Override
    public String toString() {
        return "ViaCepResponse [cep=" + cep + ", logradouro=" + logradouro + ", localidade=" + localidade + "]";
    }

    // Métodos 'getters' e 'setters'
    public String getCep() {
        return cep;
    }
    
    public void setCep(String cep) {
        this.cep = cep;
    }

    public String getLogradouro() {
        return logradouro;
    }

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public String getLocalidade() {
        return localidade;
    }

    public void setLocalidade(String localidade) {
        this.localidade = localidade;
    }
}
