package edu.dio.me.springboot.util;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class MyCommandLineRunner implements CommandLineRunner {

    @Autowired
    private Calculadora calculadora;

    @Override
    public void run(String... args) throws Exception {
        System.out.println("\nO resultado é: " + calculadora.somar(10, 5));
    }
}
