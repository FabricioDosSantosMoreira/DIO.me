package edu.me.springboot;


import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class WelcomeController {

    @GetMapping
    public String welcome() {
        return "Welcome to my Spring Boot Web API with Spring Security";
    }

    @GetMapping(path = "/users")
    @PreAuthorize("hasAnyRole('MANAGERS', 'USERS')")
    public String users() {
        return "Authorized user";
    }

    @GetMapping(path = "/managers")
    @PreAuthorize("hasAnyRole('MANAGERS')")
    public String managers() {
        return "Authorized manager";
    }
}
