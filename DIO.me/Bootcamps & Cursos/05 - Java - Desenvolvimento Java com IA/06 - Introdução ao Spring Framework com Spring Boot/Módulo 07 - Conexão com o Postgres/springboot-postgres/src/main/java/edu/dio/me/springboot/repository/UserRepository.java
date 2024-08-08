package edu.dio.me.springboot.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import edu.dio.me.springboot.model.User;

public interface UserRepository extends JpaRepository<User, Integer> {

    // Query Method
    List<User> findByNameContaining(String name);

    // Query Method
    List<User> findByUsername(String username);

    // Query Method override
    @Query("SELECT u FROM User u WHERE u.name LIKE %:name%")
    List<User> filterByName(@Param("name") String name);
}   
