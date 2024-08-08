package edu.dio.me;

public class OperadoresLogicos {

    // - - - - - > Operadores Lógicos:
    //                 Em Java, os operadores lógicos são usados para combinar e manipular expressões 
    //            booleanas. Eles ajudam a tomar decisões baseadas em múltiplas condições.
    //
    // - - - - > Exemplos de Operadores Lógicos:

    public static void main(String[] args) {
        System.out.println("\nExemplos de Operadores Lógicos:");

        boolean a = true;
        boolean b = false;

        // - - - > Operador lógico AND (&&):
        System.out.println("\nOperador lógico AND (&&):");
        
        boolean resultadoAnd = a && b;
        System.out.println("Resultado [a && b]: " + resultadoAnd);

        // - - - > Operador lógico OR (||):
        System.out.println("\nOperador lógico OR (||):");

        boolean resultadoOr = a || b;
        System.out.println("Resultado [a || b]: " + resultadoOr);

        // - - - > Operador lógico NOT (!):
        System.out.println("\nOperador lógico NOT (!):");

        boolean resultadoNotA = !a;
        boolean resultadoNotB = !b;
        System.out.println("Resultado [!a]: " + resultadoNotA);
        System.out.println("Resultado [!b]: " + resultadoNotB);

        // - - - > Operador lógico XOR (^):
        System.out.println("\nOperador lógico XOR (^):");

        boolean resultadoXor = a ^ b;
        System.out.println("Resultado [a ^ b]: " + resultadoXor);

        // - - - > Exemplo com expressões compostas:
        System.out.println("\nExemplo com expressões compostas:");

        boolean resultadoComposto = (a && !b) || (b && !a);
        System.out.println("Resultado [(a && !b) || (b && !a)]: " + resultadoComposto);
    }
}
