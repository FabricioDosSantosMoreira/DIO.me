package edu.dio.me.springboot;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import edu.dio.me.springboot.util.ViaCepResponse;
import edu.dio.me.springboot.util.GsonComponent;

@SpringBootApplication
public class Application {

	// - - - - - > Injeção de Dependências:
	// 				   No Spring Framework, a injeção de dependências (DI) e a inversão de controle (IoC) 
	//            são conceitos centrais que ajudam a gerenciar as dependências de uma aplicação. 
	//            Vamos detalhar um pouco mais sobre isso:
	//
	// - - - - > Injeção de Dependências (DI):
	//               A injeção de dependências é uma técnica onde o container do Spring fornece automaticamente 
	//           os objetos necessários (dependências) para um objeto (componente) em vez de o próprio objeto 
	//           criar ou localizar essas dependências. Isso promove um código mais modular, testável e 
	//           fácil de manter.
	//
	// - - - - > Inversão de Controle (IoC):
	//               A inversão de controle é um princípio onde o controle de criar e gerenciar objetos é 
	//           invertido. Em vez de a aplicação controlar a criação de objetos, o container IoC do 
	//           Spring é responsável por isso. O IoC Container gerencia o ciclo de vida dos beans e 
	//           injeta as dependências conforme necessário.
	//
	// - - - > Beans:
	//               Um 'bean' em Spring é um objeto que é instanciado, montado e gerenciado pelo 
	//           container Spring IoC (Inversion of Control). Beans são definidos e configurados 
	//           no contexto do Spring e são utilizados para realizar injeção de dependência.
	//           Alguns dos principais beans são:
	//
	//               - Component: Uma classe anotada com @Component é um bean genérico e pode ser usado 
	//                            para qualquer classe Spring gerenciada.
	//
	//               - Service: Uma classe anotada com @Service é usada para serviços de negócios.
	//
	//               - repository: Uma classe anotada com @Repository é usada para classes de acesso a dados.
	//
	//               - controller: Uma classe anotada com @Controller é usada para classes que lidam com a 
	//                             lógica de controle e mapeiam requisições web.
    //
	// - - - > Autowired:
	// 		        Depois de definir os beans, você pode injetá-los em outros componentes usando a anotação @Autowired.

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

	@Bean
	public CommandLineRunner run(GsonComponent conversor) throws Exception {
		return args -> {
			String json = "{\"cep\": \"01001-000\", \"logradouro\": \"Praça da Sé\", \"localidade\": \"São Paulo\"}";
			ViaCepResponse response = conversor.converter(json);

			System.out.println("\nDados do CEP: " + response);			
		};
	}
}
