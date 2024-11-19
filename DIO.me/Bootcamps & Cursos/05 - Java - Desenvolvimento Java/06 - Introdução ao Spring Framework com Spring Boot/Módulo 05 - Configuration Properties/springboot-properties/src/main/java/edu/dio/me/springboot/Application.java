package edu.dio.me.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

	// - - - - - > Configuration Properties:
	//                 Configuration properties permitem que você agrupe um conjunto de propriedades 
	//             relacionadas em uma classe POJO (Plain Old Java Object) e, assim, forneça uma 
	//             maneira mais estruturada e organizada para gerenciar as configurações. Essa 
	//             abordagem é preferida quando você tem muitas propriedades relacionadas, pois 
	//             facilita a manutenção e a clareza do código. Para usar configuration 
	//             properties, é necessário:
	//    
	//                 - Anotar a classe POJO com '@ConfigurationProperties' e '@Component' ou 
	//					 '@EnableConfigurationProperties'.
	//
	//                 - Definir as propriedades no arquivo de configuração.
	//
	//                 - Registrar a classe de configuração nas classes de configuração do Spring Boot.

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
