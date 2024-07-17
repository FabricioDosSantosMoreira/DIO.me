package edu.me.aparelho;

import edu.me.aparelho.aparelhos.IPhone;
import edu.me.aparelho.reprodutor.util.Midia;
import edu.me.aparelho.reprodutor.util.Musica;
import edu.me.aparelho.reprodutor.util.Video;


public class Celular{
    public static void main(String[] args) {

        IPhone iphone = new IPhone();

        iphone.aumentarVolume(20);
        iphone.diminuirVolume(20);

        iphone.selecionarMusica(new Musica("Spotify Music", 60, "Rock"));
        iphone.reproduzir();

        iphone.selecionarVideo(new Video("Youtube Video", 60, "1080p"));
        iphone.reproduzir();


        iphone.atender("123456789");
        iphone.ligar("123456789");
        iphone.iniciarCorreioDeVoz();

    }
}
