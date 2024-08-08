package edu.dio.me.collections.generics;

import java.util.HashSet;
import java.util.Set;

public class ExemploDeGenericSet {

	@SuppressWarnings({ "unchecked", "rawtypes" })
    public static void main(String[] args) {

        // - - - - - > Exemplo sem Generics Type:
        Set conjuntoSemGeneric = new HashSet<>();

		// OBS: Permite adicionar qualquer tipo de objeto
		conjuntoSemGeneric.add("Elemento 1");
		conjuntoSemGeneric.add(10); 

		// OBS: Necessário fazer casting
		for (Object obj : conjuntoSemGeneric) {
			String str = (String) obj.toString();
			System.out.println(str);
		}



        // - - - - - > Exemplo com Generics Type:
        Set<String> conjuntoComGeneric = new HashSet<>();

		// OBS: Permite adicionar somente String
		conjuntoComGeneric.add("Elemento 1");
		conjuntoComGeneric.add("Elemento 2");

		for (String elemento : conjuntoComGeneric) {
			System.out.println(elemento);
		}
	}
}
