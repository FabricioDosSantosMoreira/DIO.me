package edu.dio.me.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

	// - - - - - > Spring Data JPA:
	//                 Spring Data JPA é um módulo do Spring Framework que facilita a implementação 
	//             de repositórios de acesso a dados usando o padrão Java Persistence API (JPA). 
	//             Ele proporciona uma camada de abstração para as operações com o banco de dados, 
	//             permitindo trabalhar com objetos Java sem se preocupar diretamente com as 
	//             consultas SQL.
	//
	// - - - - > Principais recursos do Spring Data JPA:
	//
	// - - - > Simplificação do Acesso a Dados:
	//             Reduz significativamente a quantidade de código boilerplate necessário para realizar 
	//         operações CRUD e outras operações comuns de banco de dados.
	//
	// - - - > Repositórios:
	//             O Spring Data JPA introduz a ideia de repositórios, que são interfaces que podem ser
	//         definidas para realizar operações de banco de dados. É possível definir métodos na 
	//         interface, e o Spring Data JPA os implementará automaticamente em tempo de execução.
	//
	// - - - > Consultas Derivadas:
	//             Permite definir consultas complexas apenas declarando métodos com nomes significativos. 
	//         Por exemplo, um método 'findByLastName(String lastName)' será implementado automaticamente 
	//         para buscar registros com base no campo 'lastName'.
	//
	// - - - > Consultas com JPQL e SQL Nativo:
	//             Além das consultas derivadas, é possível usar o Java Persistence Query Language (JPQL) 
	//         ou consultas SQL nativas para operações mais complexas.
	//
	// - - - > Suporte a Transações:
	//             Facilita o gerenciamento de transações, permitindo definir a transação em um nível de 
	//         e deixe o framework gerenciá-la para você. 
	//
	// - - - > Paginação e Ordenação:
	//             Fornece suporte fácil para paginação e ordenação de resultados de consultas.

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
