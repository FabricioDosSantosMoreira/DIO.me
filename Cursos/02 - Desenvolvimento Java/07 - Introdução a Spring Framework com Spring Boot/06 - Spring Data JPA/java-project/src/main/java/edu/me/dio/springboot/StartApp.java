package edu.me.dio.springboot;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import edu.me.dio.springboot.repository.UserRepository;
import edu.me.dio.springboot.model.User;


@Component
public class StartApp implements CommandLineRunner {

    @Autowired
    private UserRepository repository;

    
    @Override
    public void run(String... args) throws Exception {
        User user = new User();
        user.setName("Test Name");
        user.setUsername("Test Username");
        user.setPassword("123456");

        repository.save(user);

        System.out.println("\n\nUsers:");
        for(User u : repository.findAll()) {
            System.out.println(u);
        }

    }
}
