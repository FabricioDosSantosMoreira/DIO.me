package edu.dio.me.modelagem.util.reprodutor;

import edu.dio.me.modelagem.util.reprodutor.util.Musica;
import edu.dio.me.modelagem.util.reprodutor.util.Video;

public interface Reprodutor extends ReprodutorMusica, ReprodutorVideo { 

    // Métodos da Interface 'Reprodutor'
    public void reproduzir();

    public void pausar();

    public void aumentarVolume(int volume);

    public void diminuirVolume(int volume);

    @Override
    public void selecionarVideo(Video video);

    @Override
    public void selecionarMusica(Musica musica);
}
