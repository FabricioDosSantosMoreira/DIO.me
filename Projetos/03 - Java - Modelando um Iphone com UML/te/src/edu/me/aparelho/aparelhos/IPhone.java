package edu.me.aparelho.aparelhos;

import java.util.Random;

import edu.me.aparelho.navegador.Navegador;
import edu.me.aparelho.reprodutor.Reprodutor;
import edu.me.aparelho.reprodutor.util.Midia;
import edu.me.aparelho.reprodutor.util.Musica;
import edu.me.aparelho.reprodutor.util.Video;
import edu.me.aparelho.telefone.Telefone;


public class IPhone implements Reprodutor, Telefone, Navegador {

    private Midia midiaAtual;
    private int volume = 10;


    public void Iphone() {}


    // Reprodutor do Iphone
    public void reproduzir() {
        if (this.midiaAtual != null) {
            System.out.println(this.midiaAtual.getTitulo()  + " Está reproduzindo!");
        } else {
            System.out.println("Nenhuma mídia foi selecionada!");
        }
    }

    public void pausar() {
        if (this.midiaAtual != null) {
            System.out.println(this.midiaAtual.getTitulo()  + " Está pausada!");
        } else {
            System.out.println("Nenhuma mídia foi selecionada!");
        }
    }

    public void aumentarVolume(int volume) {
        volume = this.volume + volume;

        System.out.println("Volume aumentado de: [" + this.volume + "] para: [" + volume + "]");
        this.volume = volume;
    }

    public void diminuirVolume(int volume) {
        volume = this.volume - volume;

        System.out.println("Volume diminuido de: [" + this.volume + "] para: [" + volume + "]");
        this.volume = volume;
    }

    @Override
    public void selecionarVideo(Video video) {
        System.out.println("Video selecionado!");
        this.midiaAtual = video;
    }

    @Override
    public void selecionarMusica(Musica musica) {
        System.out.println("Música selecionada!");
        this.midiaAtual = musica;
    }

    // Telefone do Iphone
    @Override
    public void atender(String numero) {
        System.out.println("Número [" + numero + "] foi atendido!");
    }

    @Override
    public void ligar(String numero) {
        Random random = new Random();
        boolean atendido = false;

        while(atendido == false) {
            if(random.nextInt(3) == 1) {
                atendido = true;
                System.out.println("Telefone atendido!");
                break;
            };
            System.out.println("Discando número: [" + numero + "]");
        }
    }

    @Override
    public void iniciarCorreioDeVoz() {
        System.out.println("Correio de voz reproduzindo!");
    }


    // NavegadorWeb do Iphone
    @Override
    public void exibirPagina(String url) {
        System.out.println("Página exibida!");
    }

    @Override
    public void adicionarNovaAba() {
       System.out.println("Aba adicionada!");
    }

    @Override
    public void atualizarPagina() {
        System.out.println("Página atualizada");
    }
}
