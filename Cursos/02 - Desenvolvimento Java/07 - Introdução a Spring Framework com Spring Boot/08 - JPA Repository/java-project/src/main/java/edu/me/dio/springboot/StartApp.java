package edu.me.dio.springboot;



import java.util.List;
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
        
        insertUser("User A", "Username A", "123456");
        insertUser("User B", "Username B", "123456");
        insertUser("User C", "Username C", "123456");
        insertUser("User D", "Username D", "123456");

        List<User> users = repository.findByNameContaining("User");

        System.out.println("\n\nUsers by name containing 'User':");
        for(User u: users){
            System.out.println(u);
        }

        System.out.println("\n\nUsers filtered by name 'User':");
        for(User u : repository.filterByName("User")){
            System.out.println(u);
        }

        System.out.println("\n\nUser find by name 'User A':");
        System.out.println(repository.findByUsername("Username A"));
    }

    public void insertUser(String name, String username, String password) {
        User user = new User();
        user.setName(name);
        user.setUsername(username);
        user.setPassword(password);

        repository.save(user);
    }
}
