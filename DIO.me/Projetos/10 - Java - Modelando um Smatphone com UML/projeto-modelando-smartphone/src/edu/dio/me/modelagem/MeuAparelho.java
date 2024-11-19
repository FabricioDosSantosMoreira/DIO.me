package edu.dio.me.modelagem;

import edu.dio.me.modelagem.aparelhos.Smartphone;
import edu.dio.me.modelagem.util.reprodutor.util.Musica;

public class MeuAparelho {

    public static void main(String[] args) {
        
        Smartphone smartphone = new Smartphone("0.0.1", "123456789");

        smartphone.reproduzir();
        smartphone.selecionarMusica(new Musica("Hotel California", 60, "Rock"));
        smartphone.reproduzir();
        smartphone.pausar();

        smartphone.aumentarVolume(90);
        smartphone.diminuirVolume(50);

        smartphone.ligar("987654321");
        smartphone.atender("987654321");
        smartphone.iniciarCorreioDeVoz();

        smartphone.exibirPagina("https://site.com.br");
        smartphone.adicionarNovaAba();
        smartphone.atualizarPagina();

        smartphone.atualizarVersao("1.0.0");
    }
}
