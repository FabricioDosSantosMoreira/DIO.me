package edu.dio.me.springboot.util;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class SistemaMensagem {

    @Autowired
    private Remetente noreply;
    @Autowired
    private Remetente techTeam;

    public void enviarConfirmacaoCadastro() {
       System.out.println("\nSeu cadastro foi aprovado!");
       System.out.println(noreply);
    }
    
    public void enviarMensagemBoasVindas() {
        techTeam.setEmail("Tech@teste.com.br");
        techTeam.setNome("Tech Team");
        
        System.out.println("\nBem-vindo!");
        System.out.println(techTeam);
    }
}
