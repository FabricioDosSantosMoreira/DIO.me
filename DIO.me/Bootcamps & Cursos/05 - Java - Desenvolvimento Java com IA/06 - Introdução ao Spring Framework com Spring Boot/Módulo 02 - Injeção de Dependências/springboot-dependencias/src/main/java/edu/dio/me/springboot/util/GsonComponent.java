package edu.dio.me.springboot.util;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.google.gson.Gson;

@Component
public class GsonComponent {

    @Autowired
    private Gson gson;

    public ViaCepResponse converter(String json) {
        ViaCepResponse response = gson.fromJson(json, ViaCepResponse.class);

        return response;
    }
}
