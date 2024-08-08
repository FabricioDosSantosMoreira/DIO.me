package edu.dio.me.api.service;

import edu.dio.me.api.domain.model.User;

public interface UserService {

    User findById(Long id);

    User create(User userToCreate);

}
