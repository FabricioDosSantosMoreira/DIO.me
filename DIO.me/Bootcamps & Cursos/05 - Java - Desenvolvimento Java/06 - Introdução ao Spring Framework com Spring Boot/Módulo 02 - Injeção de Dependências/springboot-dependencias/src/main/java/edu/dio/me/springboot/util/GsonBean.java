package edu.dio.me.springboot.util;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.google.gson.Gson;

@Configuration
public class GsonBean {

    @Bean
	public Gson gson() {
		return new Gson();
	}
}
