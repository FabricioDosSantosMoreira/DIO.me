package GenericsType;

import java.util.HashMap;
import java.util.Map;

public class GenericsExempleMap {

	public static void main(String[] args) {

		// Exemplo sem Generics
        // OBS: permite adicionar qualquer tipo de objeto
		Map mapaSemGenerics = new HashMap<>();
		mapaSemGenerics.put("Chave 1", 10);
		mapaSemGenerics.put("Chave 2", "valor");

		// Iterando sobre o mapa sem Generics 
		// OBS: necessário fazer cast
		for (Object obj : mapaSemGenerics.entrySet()) {
			Map.Entry entry = (Map.Entry) obj;
			String chave = (String) entry.getKey().toString();
			Object valor = entry.getValue().toString();
			System.out.println("Chave: " + chave + ", Valor: " + valor);
		}


		// Exemplo com Generics
		// OBS: permite adicionar somente String, Integer
		Map<String, Integer> mapaGenerics = new HashMap<>();
		mapaGenerics.put("Chave 1", 10);
		mapaGenerics.put("Chave 2", 20);

		// Iterando sobre o mapa com Generics
		for (Map.Entry<String, Integer> entry : mapaGenerics.entrySet()) {
			String chave = entry.getKey();
			int valor = entry.getValue();
			System.out.println("Chave: " + chave + ", Valor: " + valor);
		}
	}
}