package edu.dio.me.collections.generics;

import java.util.HashMap;
import java.util.Map;

public class ExemploDeGenericMap {

	@SuppressWarnings({ "unchecked", "rawtypes" })
    public static void main(String[] args) {

        // - - - - - > Exemplo sem Generics Type:
        Map mapaSemGeneric = new HashMap<>();

        // OBS: Permite adicionar qualquer tipo de objeto
		mapaSemGeneric.put("Chave 1", 10);
		mapaSemGeneric.put("Chave 2", "valor");

		// OBS: Necessário fazer casting
		for (Object obj : mapaSemGeneric.entrySet()) {
			Map.Entry entry = (Map.Entry) obj;
			String chave = (String) entry.getKey().toString();
			Object valor = entry.getValue().toString();

			System.out.println("Chave: " + chave + ", Valor: " + valor);
		}



        // - - - - - > Exemplo com Generics Type:
        Map<String, Integer> mapaComGeneric = new HashMap<>();

		// OBS: Permite adicionar somente chaves String e valores Integer
		mapaComGeneric.put("Chave 1", 10);
		mapaComGeneric.put("Chave 2", 20);

		for (Map.Entry<String, Integer> entry : mapaComGeneric.entrySet()) {
			String chave = entry.getKey();
			int valor = entry.getValue();

			System.out.println("Chave: " + chave + ", Valor: " + valor);
		}
	}
}
