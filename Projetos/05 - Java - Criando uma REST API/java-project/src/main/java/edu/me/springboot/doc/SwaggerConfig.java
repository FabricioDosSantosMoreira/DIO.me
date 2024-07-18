package edu.me.springboot.doc;


import java.util.Arrays;
import java.util.HashSet;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;


@Configuration
@EnableSwagger2
public class SwaggerConfig {

    private Contact contact() {
        return new Contact(
            "Contact name",
            "https://www.test.com.br",
            "test@mytest.com.br"
        );
    }

    private ApiInfoBuilder apiInfo() {

        ApiInfoBuilder apiInfoBuilder = new ApiInfoBuilder();

        apiInfoBuilder.title("Spring Boot REST API");
        apiInfoBuilder.description("REST API Using Spring Boot");
        apiInfoBuilder.version("0.1");
        apiInfoBuilder.termsOfServiceUrl("Terms of Service: Open Source");
        apiInfoBuilder.license("MIT");
        apiInfoBuilder.licenseUrl("https://mit-license.org/");
        apiInfoBuilder.contact(this.contact());

        return apiInfoBuilder;
    }

    @Bean
    public Docket apiDetail() {

        Docket docket = new Docket(DocumentationType.SWAGGER_2);

        docket
            .select()
            .apis(RequestHandlerSelectors.basePackage("edu.me.springboot.controller"))
            .paths(PathSelectors.any())
            .build()
            .apiInfo(this.apiInfo().build())
            .consumes(new HashSet<String>(Arrays.asList("application/json")))
            .produces(new HashSet<String>(Arrays.asList("application/json")));
        
        return docket;
    }
    
}
