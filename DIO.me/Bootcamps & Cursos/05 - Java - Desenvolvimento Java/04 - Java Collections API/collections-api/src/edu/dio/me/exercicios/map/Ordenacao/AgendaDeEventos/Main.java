// ├───────> Exercício - Agenda de Eventos:
// │             Crie uma classe chamada 'AgendaEventos' que utilize um `Map` para armazenar as 
// │         datas e seus respectivos Eventos. Cada evento é representado por um objeto da 
// │         classe 'Evento', que possui atributos como nome do evento e o nome da atração. 
// │         Implemente os seguintes métodos:
// │
// │             * adicionarEvento(LocalDate data, String nome, String atracao): 
// │                   Adiciona um evento à agenda.
// │
// │             * exibirAgenda(): 
// │                   Exibe a agenda de eventos em ordem crescente de data.
// │
// │             * obterProximoEvento():
// │                   Retorna o próximo evento que ocorrerá.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.map.Ordenacao.AgendaDeEventos;

import java.time.LocalDate;
import java.time.Month;

public class Main {

    public static void main(String[] args) {
        
        AgendaEventos agendaEventos = new AgendaEventos();

        // Adiciona eventos à agenda
        agendaEventos.adicionarEvento(LocalDate.of(2022, Month.JULY, 15), "Conferência de Tecnologia", "Palestrante renomado");
        agendaEventos.adicionarEvento(LocalDate.of(2022, 7, 9), "Workshop de Programação", "Aula prática de desenvolvimento");
        agendaEventos.adicionarEvento(LocalDate.of(2000, 1, 10), "Lançamento de Software", "Demonstração da nova versão");
        agendaEventos.adicionarEvento(LocalDate.of(2023, Month.AUGUST, 28), "Hackathon de Inovação", "Competição de soluções criativas");
        agendaEventos.adicionarEvento(LocalDate.of(2090, 9, 20), "Seminário de Inteligência Artificial", "Discussão sobre IA avançada");

        // Exibe a agenda completa de eventos
        agendaEventos.exibirAgenda();

        // Obtém e exibe o próximo evento na agenda
        agendaEventos.obterProximoEvento();   
    }
}
