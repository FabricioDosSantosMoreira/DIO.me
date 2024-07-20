package edu.me.service;

import edu.me.domain.model.User;

public interface UserService {

    User findById(Long id);

    User create(User userToCreate);

}
