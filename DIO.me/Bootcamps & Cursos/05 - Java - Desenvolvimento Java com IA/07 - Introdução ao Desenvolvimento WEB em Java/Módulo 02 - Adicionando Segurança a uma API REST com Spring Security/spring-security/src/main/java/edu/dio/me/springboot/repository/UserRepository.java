package edu.dio.me.springboot.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import edu.dio.me.springboot.model.User;

public interface UserRepository extends JpaRepository<User, Integer> {

    @Query("SELECT e FROM User e JOIN FETCH e.roles WHERE e.username= (:username)")
    public User findByUsername(@Param("username") String username);

    boolean existsByUsername(String username);
}
