package edu.me.domain.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import edu.me.domain.model.User;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {

}
