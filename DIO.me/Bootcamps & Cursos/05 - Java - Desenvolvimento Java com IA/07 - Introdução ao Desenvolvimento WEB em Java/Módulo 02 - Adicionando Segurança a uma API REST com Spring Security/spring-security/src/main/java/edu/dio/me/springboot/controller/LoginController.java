package edu.dio.me.springboot.controller;

import java.util.Date;

import edu.dio.me.springboot.dtos.Login;
import edu.dio.me.springboot.dtos.Sessao;
import edu.dio.me.springboot.model.User;
import edu.dio.me.springboot.repository.UserRepository;
import edu.dio.me.springboot.security.JWTCreator;
import edu.dio.me.springboot.security.JWTObject;
import edu.dio.me.springboot.security.SecurityConfig;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LoginController {

    @Autowired
    private PasswordEncoder encoder;

    @SuppressWarnings("unused")
    @Autowired
    private SecurityConfig securityConfig;

    @Autowired
    private UserRepository repository;

    @PostMapping("/login")
    public Sessao logar(@RequestBody Login login){
        User user = repository.findByUsername(login.getUsername());
    
        if(user!=null) {
            boolean passwordOk =  encoder.matches(login.getPassword(), user.getPassword());
            if (!passwordOk) {
                throw new RuntimeException("Senha inválida para o login: " + login.getUsername());
            }

            //Estamos enviando um objeto Sessão para retornar mais informações do usuário
            Sessao sessao = new Sessao();
            sessao.setLogin(user.getUsername());

            JWTObject jwtObject = new JWTObject();

            jwtObject.setIssuedAt(new Date(System.currentTimeMillis()));
            jwtObject.setExpiration((new Date(System.currentTimeMillis() + SecurityConfig.EXPIRATION)));
            jwtObject.setRoles(user.getRoles());
            sessao.setToken(JWTCreator.create(SecurityConfig.PREFIX, SecurityConfig.KEY, jwtObject));
            
            return sessao;
        }else {
            throw new RuntimeException("Erro ao tentar fazer login");
        }
    }
}
