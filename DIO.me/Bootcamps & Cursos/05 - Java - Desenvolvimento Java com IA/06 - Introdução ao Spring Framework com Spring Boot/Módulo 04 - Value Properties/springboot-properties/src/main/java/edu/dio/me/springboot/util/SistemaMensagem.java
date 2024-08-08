package edu.dio.me.springboot.util;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class SistemaMensagem implements CommandLineRunner {

	// Ver 'application.properties'
	@Value("${nome:'sem-nome'}") 
	private String nome;

	@Value("${email:'sem-email'}")
	private String email;

	@Value("${telefones}")
	private List<Long> telefones = new ArrayList<>();

	@Override
	public void run(String... args) throws Exception {
		System.out.println("\nMensagem enviada por: " + nome
						+ "\nE-mail: " + email
						+ "\nTelefones para contato: " + telefones);

		System.out.println("\nSeu cadastro foi aprovado!");
	}
}
