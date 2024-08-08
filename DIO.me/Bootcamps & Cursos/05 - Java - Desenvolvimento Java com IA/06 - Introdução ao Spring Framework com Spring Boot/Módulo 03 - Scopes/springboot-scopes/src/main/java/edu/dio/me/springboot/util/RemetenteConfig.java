package edu.dio.me.springboot.util;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;

@Configuration
public class RemetenteConfig {

    @Bean
    @Scope("singleton") // Use @Scope("prototype") ou @Scope("singleton")
    public Remetente remetente() {
        System.out.println("\nCRIANDO UM OBJETO REMETENTE");

        Remetente remetente = new Remetente();
        remetente.setEmail("Fabrício@teste.com.br");
        remetente.setNome("Fabrício");

        return remetente;
    }
}
