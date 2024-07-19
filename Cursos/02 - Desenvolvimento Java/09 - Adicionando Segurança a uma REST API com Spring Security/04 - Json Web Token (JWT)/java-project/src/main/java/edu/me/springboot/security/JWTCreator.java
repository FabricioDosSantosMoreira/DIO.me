package edu.me.springboot.security;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.ExpiredJwtException;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.MalformedJwtException;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.SignatureException;
import io.jsonwebtoken.UnsupportedJwtException;


public class JWTCreator {

    public static final String HEADER_AUTHORIZATION = "Authorization";
    public static final String ROLES_AUTHORITIES = "authorities";

    public static String create(String prefix, String key, JWTObject jwtObject) {

        System.out.println("\n\nENTREI AQUI COM prefix" + prefix);
        System.out.println("\n\nENTREI AQUI COM key" + key);
        System.out.println("\n\nENTREI AQUI COM roles" + jwtObject.getRoles());

        String token = Jwts.builder()
            .setSubject(jwtObject.getSubject())
            .setIssuedAt(jwtObject.getIssuedAt())
            .setExpiration(jwtObject.getExpiration())
            // Por algum motivo no GET /users não vem nenhum role
            .claim(ROLES_AUTHORITIES, checkRoles(Arrays.asList("USERS", "MANAGERS")))
            .signWith(SignatureAlgorithm.HS512, key)
            .compact();
            //.claim(ROLES_AUTHORITIES, checkRoles(jwtObject.getRoles())).signWith(SignatureAlgorithm.HS512, key).compact();
        
        return prefix + " " + token;
    }

    public static JWTObject create(String token, String prefix, String key)
            throws ExpiredJwtException, UnsupportedJwtException, MalformedJwtException, SignatureException {

        JWTObject object = new JWTObject();

        System.out.println("\n\n\ntoken" + token);
        System.out.println("prefix" + prefix);
        System.out.println("key" + key);

        token = create(prefix, key, object);
        token = token.replace(prefix, "");

        Claims claims = Jwts.parser().setSigningKey(key).parseClaimsJws(token).getBody();

        object.setSubject(claims.getSubject());
        object.setExpiration(claims.getExpiration());
        object.setIssuedAt(claims.getIssuedAt());
        object.setRoles((List) claims.get(ROLES_AUTHORITIES));
        
        return object;
    }

    private static List<String> checkRoles(List<String> roles) {
        if(roles == null) {
            return new ArrayList<>();
        }

        return roles.stream().map(s -> "ROLE_".concat(s.replaceAll("ROLE_",""))).collect(Collectors.toList());
    }
}
