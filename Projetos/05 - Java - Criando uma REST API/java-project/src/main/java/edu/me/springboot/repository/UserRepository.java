package edu.me.springboot.repository;


import java.util.ArrayList;
import java.util.List;
import org.springframework.stereotype.Repository;

import edu.me.springboot.handler.BusinessException;
import edu.me.springboot.handler.RequiredFieldException;
import edu.me.springboot.model.User;


@Repository
public class UserRepository {

    public void save(User user) {

        if(user.getLogin() == null) {
            throw new RequiredFieldException("login");
        }

        if(user.getPassword() == null) {
            throw new RequiredFieldException("password");
        }

        if(user.getId() == null) {
            System.out.println("\n[SAVE] - Saving user");
        } else {
            System.out.println("\n[UPDATE] - Updating user");
        }

        System.out.println("\nUSER: " + user);
    }


    public void deleteById(Integer id) {
        System.out.println("\n[DELETE/id] - id=" + id);
    }


    public List<User> findAll() {
        System.out.println("\n[LIST] - Listing all users");

        List<User> users = new ArrayList<>();
        users.add(new User("teste1", "teste1senha"));
        users.add(new User("teste2", "teste2senha"));
        users.add(new User("teste3", "teste3senha"));

        return users;
    }

    public User findById(Integer id) {
        System.out.println("\n[FIND/id] - Searching user");
        return new User("teste", "teste");
    }

    public User findByUsername(String username) {
        System.out.println("\n[FIND/username] - Searching user");
        return new User("teste", "teste");
    }

}
