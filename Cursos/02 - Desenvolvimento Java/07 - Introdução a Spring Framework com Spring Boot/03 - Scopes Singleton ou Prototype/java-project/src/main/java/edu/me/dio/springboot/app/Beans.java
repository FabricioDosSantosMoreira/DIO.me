package edu.me.dio.springboot.app;


import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;


@Configuration
public class Beans {

    @Bean
    @Scope("singleton") // Use @Scope("prototype") ou @Scope("singleton")
    public Remetente remetente() {
        System.out.println("\nCRIANDO UM OBJETO REMETENTE");

        Remetente remetente = new Remetente();
        remetente.setEmail("you@edu.me.com.br");
        remetente.setNome("Fabrício");

        return remetente;
    }
}
