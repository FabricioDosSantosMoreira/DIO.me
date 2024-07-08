package GenericsType;

import java.util.ArrayList;
import java.util.List;


public class GenericsExampleList {
    public static void main(String[] args) {

        // Exemplo sem Generics
        // OBS: permite adicionar qualquer tipo de objeto
        List listaSemGenerics = new ArrayList<>();
        listaSemGenerics.add("Elemento 1");
        listaSemGenerics.add(10);

        // Iterando sobre a lista sem Generics
        // OBS: necessário fazer cast
        for (Object elemento : listaSemGenerics) {
            String str = (String) elemento.toString();
            System.out.println(str);
        }


        // Exemplo com Generics
        // OBS: permite adicionar somente String
        List<String> listaComGenerics = new ArrayList<>();
        listaComGenerics.add("Elemento 1");
        listaComGenerics.add("Elemento 2");

        // Iterando sobre a lista com Generics
        for (String elemento : listaComGenerics) {
            System.out.println(elemento);
        }
    }
}
