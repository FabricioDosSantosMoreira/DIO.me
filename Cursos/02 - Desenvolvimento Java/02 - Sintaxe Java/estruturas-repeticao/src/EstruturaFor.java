public class EstruturaFor {

    public static void main(String[] args) {
        
        // for
        System.out.println();

        for(int i=0; i <= 10; i++) {
            System.out.println(i);
        }
        for (int carneirinhos = 1; carneirinhos <= 100; carneirinhos++) {
            System.out.println(carneirinhos + " Carneirinhos!");
        } 


        // For em Arrays
        String letras[] = {"A", "B", "C", "D", "E", "F", "G"};

        for (int i=0; i < letras.length; i ++) {
            System.out.println("Index: " + i + " Letra: " + letras[i]);
        }

        // for each
        for (String letra : letras) {
            System.out.println("Letra: " + letra);
        }


        // break e continue
        // O comando break interrompe o laço, ja o continue interrompe somente o loop atual
        for (int i = 0; i <= 10; i++) {
            if(i == 5) {
                break; // Vai parar de printar
            }    
            if(i == 3) {
                continue; // Não vai printar o 3
            }
            System.out.println("Break: " + i);
        }
    }
}
