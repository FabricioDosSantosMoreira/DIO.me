package GenericsType;

import java.util.HashSet;
import java.util.Set;

public class GenericsExempleSet {
	public static void main(String[] args) {

		// Exemplo sem Generics
		// OBS: permite adicionar qualquer tipo de objeto
		Set conjuntoSemGenerics = new HashSet<>();
		conjuntoSemGenerics.add("Elemento 1");
		conjuntoSemGenerics.add(10); 

		// Iterando sobre o conjunto sem Generics 
		// OBS: necessário fazer cast
		for (Object elemento : conjuntoSemGenerics) {
			String str = (String) elemento.toString();
			System.out.println(str);
		}


		// Exemplo com Generics
		// OBS: permite adicionar somente String
		Set<String> conjuntoGenerics = new HashSet<>();
		conjuntoGenerics.add("Elemento 1");
		conjuntoGenerics.add("Elemento 2");

		// Iterando sobre o conjunto com Generics
		for (String elemento : conjuntoGenerics) {
			System.out.println(elemento);
		}
	}
}