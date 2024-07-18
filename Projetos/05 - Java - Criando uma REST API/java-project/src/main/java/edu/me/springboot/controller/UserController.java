package edu.me.springboot.controller;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import edu.me.springboot.model.User;
import edu.me.springboot.repository.UserRepository;


@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserRepository repository;

    @GetMapping()
    public List<User> getUsers() {
        return repository.findAll();
    }

    @GetMapping(path = "/{username}")
    public User getUser(@PathVariable("username") String username) {
        return repository.findByUsername(username);
    }

    @DeleteMapping(path = "/{id}")
    public void deleteUser(@PathVariable("id") Integer id) {
        repository.deleteById(id);
    }

    @PostMapping()
    public void postUser(@RequestBody User user) {
        repository.save(user);
    }

}
