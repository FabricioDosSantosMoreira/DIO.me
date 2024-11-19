package edu.dio.me.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

    // - - - - - > Spring Framework:
    //                 O Spring Framework é um framework abrangente e modular para o 
    //             desenvolvimento de aplicações Java. Ele fornece uma ampla gama de 
    //             funcionalidades que facilitam o desenvolvimento, a configuração e 
    //             a manutenção de aplicativos. Algumas características principais
    //             do Spring Framework incluem:
    //
    //                 - Injeção de Dependência (DI) e Inversão de Controle (IoC)
    //
    //                 - Aspect-Oriented Programming (AOP)
    //
    //                 - Programação Orientada a Eventos
    //
    //                 - MVC (Model-View-Controller)
    //
    //                 - Gerenciamento de Transações
    //      
    // - - - - > Spring Boot:
    //               O Spring Boot é uma extensão do Spring Framework que visa simplificar 
    //           a configuração e o desenvolvimento de novos aplicativos Spring. Ele reduz 
    //           a quantidade de configuração necessária e facilita o início rápido de 
    //           novos projetos.
    
    public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
