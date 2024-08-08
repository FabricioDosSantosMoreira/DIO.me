package edu.dio.me.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

	// H2 database console default url: http://localhost:8080/h2-console/
	
	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

	// Adicionando um admin
	// POST http://localhost:8080/users
	// Body: {"name": "admin", "username": "admin", "password": "admin","roles": ["USERS", "MANAGERS"]}

	// Buscando um admin
	// POST http://localhost:8080/login
	// Body: {"username": "admin", "password": "admin"}

	// Acessando o admin
	// GET http://localhost:8080/users ou GET http://localhost:8080/managers
	// Authorization: Bearer ...

	// Adicionando um usuário
	// POST http://localhost:8080/users
	// Body: 
	// {"name": "user", "username": "username", "password": "123456", "roles": ["USERS"]}

	// Buscando um usuário
	// POST http://localhost:8080/login
	// Body: {"username": "username", "password": "123456"}

	// Acessando o usuário
	// GET http://localhost:8080/users
	// Authorization: Bearer ...
}
