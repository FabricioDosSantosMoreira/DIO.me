package edu.dio.me.springboot;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import edu.dio.me.springboot.util.SistemaMensagem;

@SpringBootApplication
public class Application {

	// - - - - - > Scopes:
	//                 Em Spring Boot, os 'scopes' determinam o ciclo de vida e a visibilidade dos beans 
	//             no contêiner de IoC (Inversion of Control). Existem vários tipos de scopes que podem 
	//             ser usados, cada um definindo um ciclo de vida diferente para os beans.
	//
	// - - - - > Scopes comuns em Spring:
	//
	// - - - > Singleton:
	//             Este é o scope padrão. Um bean com este escopo terá uma única instância para o contêiner 
	//         de IoC durante toda a execução da aplicação. É usado quando você quer que uma única instância 
	//         do bean seja compartilhada e reutilizada em toda a aplicação. 
	//         É definido usando @Scope("singleton").
	//
	// - - - > Prototype:
	//             Um bean com este escopo terá uma nova instância cada vez que for solicitado do contêiner.
	//         É usado quando você precisa de uma nova instância do bean toda vez que ele é solicitado, 
	//         por exemplo, quando os dados mantidos pelo bean são específicos para uma operação única.
	//         É definido usando @Scope("prototype").
	//
	// - - - > Request:
	//             Um bean com este escopo é criado e vinculado ao ciclo de vida de uma única solicitação HTTP. 
	//         Cada solicitação terá sua própria instância do bean. É usado em aplicações web para garantir 
	//         que um bean seja instanciado uma vez por solicitação HTTP.
	//         É definido usando @Scope("request").
	//
	// - - - > Session:
	//             Um bean com este escopo é criado e vinculado ao ciclo de vida de uma sessão HTTP. Cada sessão 
	//         terá sua própria instância do bean. É usado em aplicações web para dados que devem persistir 
	//         durante a sessão do usuário, como informações de login. 
	//         É definido usando @Scope("session").
	//
	// - - - > Application:
	//             Um bean com este escopo é criado e vinculado ao ciclo de vida do contexto de servlet. Este escopo 
	//        é similar ao singleton, mas o bean é único em toda a aplicação web. É usado quando você quer que um 
	//        bean seja compartilhado em toda a aplicação web.
	//        É definido usando @Scope("application").
	//
    // - - - > WebSocket:
	//             Um bean com este escopo é criado e vinculado ao ciclo de vida de uma sessão WebSocket. É usado
	//         para aplicações que utilizam WebSockets para comunicação em tempo real.
	//        É definido usando @Scope("websocket").

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

	@Bean
	public CommandLineRunner run(SistemaMensagem sistema) throws Exception {
		return args -> {
			sistema.enviarConfirmacaoCadastro();
			sistema.enviarMensagemBoasVindas();
			sistema.enviarConfirmacaoCadastro();
		};
	}
}
