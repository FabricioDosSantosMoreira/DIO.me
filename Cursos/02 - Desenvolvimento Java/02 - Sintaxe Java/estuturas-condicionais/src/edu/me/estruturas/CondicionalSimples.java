package edu.me.estruturas;

public class CondicionalSimples {

    public static void main(String[] args) {
        
        double saldo = 25.0;
        double valorSolicitado = 10.0;

        if(valorSolicitado < saldo) {
            saldo = saldo - valorSolicitado;
        }
        System.out.println("\nSaldo atual: " + saldo);
        

    }









    

}
