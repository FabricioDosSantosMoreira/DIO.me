package edu.me.springboot;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

	// Adicionando um admin
	// POST http://localhost:8080/users
	// Body:
	// {"name": "admin", "username": "admin", "password": "admin","roles": ["USERS", "MANAGERS"]}

	// Adicionando um usuário
	// POST http://localhost:8080/users
	// Body: 
	// {"name": "user", "username": "username", "password": "123456","roles": ["USERS"]}

	// Buscando um usuário
	// POST http://localhost:8080/login
	// Body:
	// {"username": "admin", "password": "admin"}

	// Acessando o usuário
	// GET http://localhost:8080/users
	// Body:
	//
}
