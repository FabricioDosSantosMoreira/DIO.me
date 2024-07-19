package edu.me.springboot.service;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import edu.me.springboot.model.User;
import edu.me.springboot.repository.UserRepository;


@Service
public class UserService {

    @Autowired
    private UserRepository repository;

    @Autowired
    private PasswordEncoder encoder;

    public void createUser(User user) {
        String password = user.getPassword();

        // Criptografando antes de salvar no banco
        user.setPassword(encoder.encode(password));
        repository.save(user);
    }
}
