package edu.me.service.impl;

import java.util.NoSuchElementException;

import org.springframework.stereotype.Service;

import edu.me.domain.model.User;
import edu.me.domain.repository.UserRepository;
import edu.me.service.UserService;

@Service
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;

    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public User findById(Long id) {
        return userRepository.findById(id).orElseThrow(NoSuchElementException::new);
    }

    @Override
    public User create(User userToCreate) {
        if(userToCreate.getId() != null && userRepository.existsById(userToCreate.getId())) {
            throw new IllegalArgumentException("This User id already exists.");

        } else if(userRepository.existsByAccountNumber(userToCreate.getAccount().getNumber())) {
            throw new IllegalArgumentException("This User account number already exists.");
        }

        return userRepository.save(userToCreate);
    }

}
