package edu.dio.me.springboot.model;

public class User {

    // Atributos
    private Integer id;
    private String login;
    private String password;

    // Método construtor vazio
    public User() {}

    // Método construtor completo
    public User(Integer id, String login, String password) {
        this.id = id;
        this.login = login;
        this.password = password;
    }

    // Método 'toString()'
    @Override
    public String toString() {
        return "User{'id': " + this.getId() + ", 'login': " + this.getLogin() + ", 'password': " + this.getPassword() + "}";
    }

    // Métodos 'getters' e 'setters'
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
