package edu.me.springboot.handler;


public class RequiredFieldException extends BusinessException {

    public RequiredFieldException(String field) {
        super(String.format("The field %s is required!", field));
    }

}
