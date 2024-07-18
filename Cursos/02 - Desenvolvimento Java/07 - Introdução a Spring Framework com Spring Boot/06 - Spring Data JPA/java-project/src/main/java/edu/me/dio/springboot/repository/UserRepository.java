package edu.me.dio.springboot.repository;


import org.springframework.data.jpa.repository.JpaRepository;
import edu.me.dio.springboot.model.User;


public interface UserRepository extends JpaRepository<User, Integer> {}
