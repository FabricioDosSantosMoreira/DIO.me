package edu.me.aparelho.reprodutor;


public interface ReprodutorMidia { 

    public abstract void reproduzir();
    public abstract void pausar();

    public void aumentarVolume(int volume);
    public void diminuirVolume(int volume);

}