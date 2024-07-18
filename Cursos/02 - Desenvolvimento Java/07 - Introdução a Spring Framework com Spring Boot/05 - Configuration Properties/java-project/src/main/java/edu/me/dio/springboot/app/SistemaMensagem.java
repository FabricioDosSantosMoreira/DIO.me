package edu.me.dio.springboot.app;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;


@Component
public class SistemaMensagem implements CommandLineRunner {

	@Autowired
	private Rementente rementente;

	@Override
	public void run(String... args) throws Exception {
		System.out.println("\nMensagem enviada por: " + rementente.getNome() + 
				"\nE-mail: " + rementente.getEmail() + 
				"\nTelefones para contato: " + rementente.getTelefones());

		System.out.println("\nSeu cadastro foi aprovado");
	}
}
