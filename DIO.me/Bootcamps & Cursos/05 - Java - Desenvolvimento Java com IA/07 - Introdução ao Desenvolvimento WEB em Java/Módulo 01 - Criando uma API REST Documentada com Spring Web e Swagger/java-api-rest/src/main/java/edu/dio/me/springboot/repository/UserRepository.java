package edu.dio.me.springboot.repository;

import java.util.ArrayList;
import java.util.List;
import org.springframework.stereotype.Repository;

import edu.dio.me.springboot.handler.RequiredFieldException;
import edu.dio.me.springboot.model.User;

@Repository
public class UserRepository {

    public void save(User user) {
        if(user.getId() == null) {
            throw new RequiredFieldException("id");
        }
        if(user.getLogin() == null) {
            throw new RequiredFieldException("login");
        }
        if(user.getPassword() == null) {
            throw new RequiredFieldException("password");
        }

        System.out.println("\n[SAVE] - Saving user\n" + user);
    }


    public void updateById(User user) {
        if(user.getId() == null) {
            throw new RequiredFieldException("id");
        }
        if(user.getLogin() == null) {
            throw new RequiredFieldException("login");
        }
        if(user.getPassword() == null) {
            throw new RequiredFieldException("password");
        }

        System.out.println("\n[UPDATE] - Updating user\n" + user);
    }


    public void deleteById(Integer id) {
        System.out.println("\n[DELETE BY ID] - Deleting user with id=" + id);
    }


    public List<User> findAll() {
        System.out.println("\n[FIND ALL] - Listing all users");

        List<User> users = new ArrayList<>();
        users.add(new User(1, "loginTeste1", "senhaTeste1"));
        users.add(new User(2, "loginTeste2", "senhaTeste2"));
        users.add(new User(3, "loginTeste3", "senhaTeste3"));

        // Simulando o retorno de uma lista de 'User'
        return users;
    }

    public User findById(Integer id) {
        System.out.println("\n[FIND BY ID] - Searching user with id=" + id);

        // Simulando o retorno de um 'User'
        return new User(1, "loginTeste", "senhaTeste");
    }

    public User findByUsername(String username) {
        System.out.println("\n[FIND BY USERNAME] - Searching user with username=" + username);
        
        // Simulando o retorno de um 'User'
        return new User(1, "loginTeste", "senhaTeste");
    }
}
