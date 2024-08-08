// ├───────> Exercício - Agenda de Contatos:
// │             Crie uma classe chamada 'AgendaContatos' que utilize um Map para armazenar os 
// │         contatos. Cada contato possui um nome como chave e um número de telefone como 
// │         valor. Implemente os seguintes métodos:
// │
// │            * adicionarContato(String nome, Integer telefone): 
// │                  Adiciona um contato à agenda, associando o nome do contato ao número de 
// │                  telefone correspondente.
// │
// │            * removerContato(String nome): 
// │                  Remove um contato da agenda, dado o nome do contato.
// │
// │            * exibirContatos():
// │                  Exibe todos os contatos da agenda, mostrando o nome e o número de telefone 
// │                  de cada contato.
// │
// │            * pesquisarPorNome(String nome):
// │                  Pesquisa um contato pelo nome e retorna o número de telefone correspondente.
// │
// │
// │
// └───────> Código:

package edu.dio.me.exercicios.map.Basico.AgendaDeContatos;

public class Main {
    
    public static void main(String[] args) {
        
        // Instânciando um objeto da classe 'agendaContatos'
        AgendaContatos agendaContatos = new AgendaContatos();

        // Adicionando contatos
        agendaContatos.adicionarContato("Camila", 123456);
        // OBS: o contato 'Camila' será atualizado
        agendaContatos.adicionarContato("Camila", 44444);
        agendaContatos.adicionarContato("João", 5665);
        agendaContatos.adicionarContato("Carlos", 1111111);
        agendaContatos.adicionarContato("Ana", 654987);
        agendaContatos.adicionarContato("Maria", 1111111);
        
        // Exibindo contatos
        agendaContatos.exibirContatos();

        // Remover um contato
        agendaContatos.removerContato("Maria");
        agendaContatos.exibirContatos();

        // Pesquisar número por nome
        String nomePesquisa = "João";
        Integer numeroPesquisa = agendaContatos.pesquisarPorNome("João");
        System.out.println("Número de telefone de " + nomePesquisa + ": " + numeroPesquisa);

        String nomePesquisaNaoExistente = "Paula";
        Integer numeroPesquisaNaoExistente = agendaContatos.pesquisarPorNome(nomePesquisaNaoExistente);
        System.out.println("Número de telefone de " + nomePesquisaNaoExistente + ": " + numeroPesquisaNaoExistente);
    }
}
