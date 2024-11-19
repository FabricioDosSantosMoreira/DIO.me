package edu.dio.me.gof.facade;

public class SubSistema2 {

    private static SubSistema2 instancia = new SubSistema2();

    private SubSistema2() {
        super();
    }

    public static SubSistema2 getInstancia() {
        return instancia;
    }

    public String recuperarCidade(String cep) {
        System.out.println("\nRecuperando cidade via SubSistema2");
        return "Cidade";
    }

    public String recuperarEstado(String cep) {
        System.out.println("\nRecuperando estado via SubSistema2");
        return "Estado";
    }
}
