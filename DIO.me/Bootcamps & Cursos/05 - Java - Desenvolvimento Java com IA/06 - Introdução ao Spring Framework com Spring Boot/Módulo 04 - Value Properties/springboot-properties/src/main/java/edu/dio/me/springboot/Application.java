package edu.dio.me.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {
	
	// - - - - - > Value Properties:
	//                 Value properties são propriedades que você define em arquivos de configuração 
	//             como 'application.properties' ou 'application.yml' e que podem ser injetadas 
	//             diretamente em componentes Spring usando a anotação '@Value'.

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
