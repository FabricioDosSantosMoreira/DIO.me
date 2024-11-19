package edu.dio.me.springboot.doc;

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

    private static final String BASE_PACKAGE = "edu.dio.me.springboot.controller";
    private static final String MEDIA_TYPE_JSON = "application/json";

    private Contact contact() {
        return new Contact(
            "your name here",
            "your url here",
            "your email here"
        );
    }

    private ApiInfoBuilder apiInfo() {

        ApiInfoBuilder apiInfoBuilder = new ApiInfoBuilder();

        apiInfoBuilder.title("Spring Boot REST API");
        apiInfoBuilder.description("REST API Using Spring Boot");
        apiInfoBuilder.version("0.1");
        apiInfoBuilder.license("MIT");
        apiInfoBuilder.contact(this.contact());
        apiInfoBuilder.licenseUrl("https://mit-license.org/");
        apiInfoBuilder.termsOfServiceUrl("Terms of Service: Open Source");
        
        return apiInfoBuilder;
    }

    @Bean
    public Docket apiDetail() {

        Docket docket = new Docket(DocumentationType.SWAGGER_2);

        docket
            .select()
            .apis(RequestHandlerSelectors.basePackage(BASE_PACKAGE))
            .paths(PathSelectors.any())
            .build()
            .apiInfo(this.apiInfo().build())
            .consumes(new HashSet<String>(Arrays.asList(MEDIA_TYPE_JSON)))
            .produces(new HashSet<String>(Arrays.asList(MEDIA_TYPE_JSON)));
        
        return docket;
    }
}
