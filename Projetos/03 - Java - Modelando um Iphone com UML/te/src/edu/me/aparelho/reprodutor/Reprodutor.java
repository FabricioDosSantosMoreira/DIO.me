package edu.me.aparelho.reprodutor;

import edu.me.aparelho.reprodutor.util.Musica;
import edu.me.aparelho.reprodutor.util.Video;


public interface Reprodutor extends ReprodutorMusica, ReprodutorVideo { 

    public void reproduzir();

    public void pausar();

    public void aumentarVolume(int volume);

    public void diminuirVolume(int volume);

    @Override
    public void selecionarVideo(Video video);

    @Override
    public void selecionarMusica(Musica musica);
}
