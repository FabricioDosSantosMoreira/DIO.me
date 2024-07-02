package edu.me.sintaxe;

public class SmartTV {

    boolean ligada;
    int canal;
    int volume;

    // Construtor completo da classe 'SmartTV'
    public SmartTV(boolean ligada, int canal, int volume) {
        this.ligada = ligada;
        this.canal = canal;
        this.volume = volume;
    }

    public void ligar() {
        setLigada(true);
    }

    public void desligar() {
        setLigada(false);
    }

    public void mudarVolume(int volume) {
        setVolume(volume);
    }

    public void aumentarVolume() {
        setVolume(++ this.volume);
    }

    public void diminuirVolume() {
        setVolume(getVolume() - 1);
    }

    public void mudarCanal(int canal) {
        setCanal(canal);
    }


    // Getters e Setters
    public boolean isLigada() {
        return ligada;
    }

    public void setLigada(boolean ligada) {
        this.ligada = ligada;
    }

    public int getCanal() {
        return canal;
    }

    public void setCanal(int canal) {
        this.canal = canal;
    }

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }

}
