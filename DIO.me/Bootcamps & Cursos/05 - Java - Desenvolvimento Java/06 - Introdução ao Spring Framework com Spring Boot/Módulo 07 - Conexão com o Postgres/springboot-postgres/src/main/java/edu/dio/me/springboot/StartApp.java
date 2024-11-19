package edu.dio.me.springboot;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import edu.dio.me.springboot.repository.UserRepository;
import edu.dio.me.springboot.model.User;

@Component
public class StartApp implements CommandLineRunner {

    @Autowired
    private UserRepository userRepository;

    @Override
    public void run(String... args) throws Exception {
    
        insertUser("User A", "Username A", "123456");
        insertUser("User B", "Username B", "123456");
        insertUser("User C", "Username C", "123456");
        insertUser("User D", "Username D", "123456");

        System.out.println("\nQuery method 'findAll':");
        for(User u : userRepository.findAll()) {
            System.out.println(u);
        }
 
        List<User> users = userRepository.findByNameContaining("User");
        System.out.println("\nQuery method 'findByNameContaining':");
        for(User u: users){
            System.out.println(u);
        }

        System.out.println("\nQuery method 'filterByName':");
        for(User u : userRepository.filterByName("User")){
            System.out.println(u);
        }

        System.out.println("\nQuery method 'findByUsername':");
        for(User u : userRepository.findByUsername("Username A")){
            System.out.println(u);
        }
    }

    public void insertUser(String name, String username, String password) {
        User user = new User();
        user.setName(name);
        user.setUsername(username);
        user.setPassword(password);

        userRepository.save(user);
    }
}
