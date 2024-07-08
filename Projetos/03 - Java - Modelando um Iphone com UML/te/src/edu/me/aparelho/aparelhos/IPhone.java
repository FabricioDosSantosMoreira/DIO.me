package edu.me.aparelho.aparelhos;

import edu.me.aparelho.reprodutor.ReprodutorMusica;
import edu.me.aparelho.reprodutor.ReprodutorVideo;


public class IPhone implements ReprodutorMusica, ReprodutorVideo {

    @Override
    public void reproduzir() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'reproduzir'");
    }

    @Override
    public void pausar() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'pausar'");
    }

    @Override
    public void aumentarVolume(int volume) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'aumentarVolume'");
    }

    @Override
    public void diminuirVolume(int volume) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'diminuirVolume'");
    }

    @Override
    public void selecionarVideo(String video) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'selecionarVideo'");
    }

    @Override
    public void selecionarMusica(String musica) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'selecionarMusica'");
    }
    
}
