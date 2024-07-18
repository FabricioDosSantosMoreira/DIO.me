package edu.me.dio.springboot.app;


import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;


@Component
public class SistemaMensagem implements CommandLineRunner {

	@Value("${nome}") // @Value("${nome:algum valor padrão aqui caso 'application.properties' sem valor correspondente}")
	private String nome;
	@Value("${email}")
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
