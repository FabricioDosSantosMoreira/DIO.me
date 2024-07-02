package edu.me.sintaxe;

public class SmartTvUsuario {
    public static void main(String[] args) {

        SmartTV smartTV = new SmartTV(false, 1, 10);
        

        System.out.println("TV ligada? " + smartTV.isLigada());
        System.out.println("Canal atual: " + smartTV.getCanal());
        System.out.println("Volume atual: " + smartTV.getVolume());

        smartTV.ligar();
        System.out.println("TV ligada? " + smartTV.isLigada());
        smartTV.desligar();
        System.out.println("TV ligada? " + smartTV.isLigada());

        smartTV.mudarVolume(9);
        System.out.println("Volume atual: " + smartTV.getVolume());
        smartTV.aumentarVolume();
        System.out.println("Volume atual: " + smartTV.getVolume());
        smartTV.diminuirVolume();
        System.out.println("Volume atual: " + smartTV.getVolume());

        smartTV.mudarCanal(35);
        System.out.println("Canal atual: " + smartTV.getCanal());

    }
}