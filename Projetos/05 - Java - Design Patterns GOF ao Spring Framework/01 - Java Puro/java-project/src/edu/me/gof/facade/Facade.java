package edu.me.gof.facade;

public class Facade {

    public void migrarCliente(String nome, String cep) {

        String estado = SubSistema2.getInstancia().recuperarEstado(cep);
        String cidade = SubSistema2.getInstancia().recuperarCidade(cep);

        SubSistema1.gravarCliente(nome, cep, estado, cidade);

        System.out.println("Migrando cliente: [" + nome + ", " + cep + ", " + estado + ", " + cidade +"]");
    }
}
