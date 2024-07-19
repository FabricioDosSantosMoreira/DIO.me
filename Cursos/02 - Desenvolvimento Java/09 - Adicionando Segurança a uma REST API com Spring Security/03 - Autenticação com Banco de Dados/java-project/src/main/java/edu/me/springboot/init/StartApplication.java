package edu.me.springboot.init;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import edu.me.springboot.model.User;
import edu.me.springboot.repository.UserRepository;


@Component
public class StartApplication implements CommandLineRunner {

    @Autowired
    private UserRepository repository;

    @Transactional
    @Override
    public void run(String... args) throws Exception {
        User user = repository.findByUsername("admin");
        if(user == null) {
            user = new User();
            user.setName("ADMIN");
            user.setUsername("admin");
            user.setPassword("123456");
            user.getRoles().add("MANAGERS");

            repository.save(user);
        }

        user = repository.findByUsername("user");
        if(user == null) {
            user = new User();
            user.setName("USER");
            user.setUsername("user");
            user.setPassword("123456");
            user.getRoles().add("USERS");

            repository.save(user);
        }
    }
}
