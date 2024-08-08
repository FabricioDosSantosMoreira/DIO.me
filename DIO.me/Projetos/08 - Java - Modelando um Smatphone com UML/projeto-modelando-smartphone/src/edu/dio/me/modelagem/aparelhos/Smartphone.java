package edu.dio.me.modelagem.aparelhos;

import java.util.Random;

import edu.dio.me.modelagem.util.navegador.Navegador;
import edu.dio.me.modelagem.util.os.SistemaOperacional;
import edu.dio.me.modelagem.util.reprodutor.Reprodutor;
import edu.dio.me.modelagem.util.reprodutor.util.Midia;
import edu.dio.me.modelagem.util.reprodutor.util.Musica;
import edu.dio.me.modelagem.util.reprodutor.util.Video;
import edu.dio.me.modelagem.util.telefone.Telefone;

public class Smartphone implements SistemaOperacional, Telefone, Navegador, Reprodutor {

    // Atributos da classe 'Smatphone'
    private String versao_os;
    private String numero;
    private int volume;
    private Midia midiaAtual;

    // Método construtor da classe 'Smatphone'
    public Smartphone(String versao_os, String numero) {
        this.versao_os = versao_os;
        this.numero = numero;
    }

    // Métodos do 'Reprodutor' do 'Smatphone'
    @Override
    public void reproduzir() {
        if (this.midiaAtual != null) {
            System.out.println(this.midiaAtual.getTitulo()  + " Está reproduzindo!");
        } else {
            System.out.println("Nenhuma mídia foi selecionada!");
        }
    }

    @Override
    public void pausar() {
        if (this.midiaAtual != null) {
            System.out.println(this.midiaAtual.getTitulo()  + " Está pausada!");
        } else {
            System.out.println("Nenhuma mídia foi selecionada!");
        }
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

    @Override
    public void aumentarVolume(int volume) {
        volume = this.volume + volume;

        System.out.println("Volume aumentado de: [" + this.volume + "] para: [" + volume + "]");
        this.volume = volume;
    }

    @Override
    public void diminuirVolume(int volume) {
        volume = this.volume - volume;

        System.out.println("Volume diminuido de: [" + this.volume + "] para: [" + volume + "]");
        this.volume = volume;
    }

    // Métodos do 'Telefone' do 'Smatphone'
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

    // Métodos do 'Navegador' do 'Smatphone'
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
        System.out.println("página atualizada!");
    }

    // Métodos do 'Navegador' do 'Smatphone'
    @Override
    public boolean atualizarVersao(String versao) {
        this.versao_os = versao;
        System.out.println("Versão do OS atualizada!");

        return true;
    }
}
