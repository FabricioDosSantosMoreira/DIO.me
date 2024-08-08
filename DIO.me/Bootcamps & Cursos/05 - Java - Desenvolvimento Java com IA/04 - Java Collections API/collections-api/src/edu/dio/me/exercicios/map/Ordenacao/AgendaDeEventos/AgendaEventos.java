package edu.dio.me.exercicios.map.Ordenacao.AgendaDeEventos;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class AgendaEventos {

    // Atributo da classe 'AgendaEventos'
    private Map<LocalDate, Evento> agendaEventos;

    // Método construtor da classe 'AgendaEventos'
    public AgendaEventos() {
        this.agendaEventos = new HashMap<>();
    }

    // Métodos da classe 'AgendaEventos'
    public void adicionarEvento(LocalDate data, String nome, String atracao) {
        this.agendaEventos.put(data, new Evento(nome, atracao));
    }    

    public void exibirAgenda() {
        // Cria um TreeMap que ordena pelo LocalDate
        Map<LocalDate, Evento> agendaOrdenada = new TreeMap<>(this.agendaEventos);

        for (Map.Entry<LocalDate, Evento> entry : agendaOrdenada.entrySet()) {
            LocalDate dataEvento = entry.getKey();
            Evento evento = entry.getValue();

            System.out.println("Data: " + dataEvento + ", Evento: " + evento.getNome() + ", Atração: " + evento.getAtracao());
        }
    }

    public void obterProximoEvento() {
        LocalDate dataAtual = LocalDate.now();
        LocalDate proximaData = null;
        Evento proximoEvento = null;

        for (Map.Entry<LocalDate, Evento> entry : this.agendaEventos.entrySet()) {
            LocalDate dataEvento = entry.getKey();

            if (dataEvento.isEqual(dataAtual) || dataEvento.isAfter(dataAtual)) {
                proximaData = dataEvento;
                proximoEvento = entry.getValue();
                break;
            }
        }

        if (proximoEvento != null) {
            System.out.println("O próximo evento: " + proximoEvento.getNome() + " acontecerá na data " + proximaData);
        } else {
             System.out.println("\nNão há eventos futuros na agenda.");
        }
    }
}
