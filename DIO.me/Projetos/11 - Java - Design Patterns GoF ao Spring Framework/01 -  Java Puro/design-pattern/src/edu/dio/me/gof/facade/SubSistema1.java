package edu.dio.me.gof.facade;

public class SubSistema1 {

    private SubSistema1() {
        super();
    }

    public static void gravarCliente(String nome, String cep, String estado, String cidade) {
        System.out.println("\nGravando cliente: " + nome);
        System.out.println("Cliente salvo via SubSistema1");
    }
}