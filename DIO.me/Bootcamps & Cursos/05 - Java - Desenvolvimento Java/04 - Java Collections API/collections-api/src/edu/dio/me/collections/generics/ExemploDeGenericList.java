package edu.dio.me.collections.generics;

import java.util.ArrayList;
import java.util.List;

public class ExemploDeGenericList {

    @SuppressWarnings({ "unchecked", "rawtypes" })
    public static void main(String[] args) {

        // - - - - - > Exemplo sem Generics Type:
        List listaSemGeneric = new ArrayList<>();

        // OBS: Permite adicionar qualquer tipo de objeto
        listaSemGeneric.add("Elemento 1"); 
        listaSemGeneric.add(10);

        // OBS: Necessário fazer casting
        for (Object obj : listaSemGeneric) {
            String str = (String) obj.toString();
            System.out.println(str);
        }



        // - - - - - > Exemplo com Generics Type:
        List<String> listaComGeneric = new ArrayList<>();

        // OBS: Permite adicionar somente String
        listaComGeneric.add("Elemento 1");
        listaComGeneric.add("Elemento 2");

        for (String elemento : listaComGeneric) {
            System.out.println(elemento);
        }
    }
}
