// Conjunto de Convidados
// Crie uma classe chamada "ConjuntoConvidados" que possui um conjunto de objetos do tipo "Convidado" como atributo. Cada convidado possui atributos como nome e código do convite. Implemente os seguintes métodos:

// adicionarConvidado(String nome, int codigoConvite): Adiciona um convidado ao conjunto.
// removerConvidadoPorCodigoConvite(int codigoConvite): Remove um convidado do conjunto com base no código do convite.
// contarConvidados(): Conta o número total de convidados no Set.
// exibirConvidados(): Exibe todos os convidados do conjunto.

package SetInterface.Exercicios.Basico.ConjuntoDeConvidados;

public class Main {
    public static void main(String[] args) {
        
        // Instânciando um objeto da classe 'ConjuntoConvidados'
        ConjuntoConvidados convidados = new ConjuntoConvidados();

        // Exibindo o número de convidados
        System.out.println("\nExistem " + convidados.contarConvidados() + " convidado(s) dentro do Set de Convidados");

        // Adicionando convidados 
        convidados.adicionarConvidado("Alice", 1234);
        convidados.adicionarConvidado("Bob", 1235);
        // Este convidado não será salvo, pois o codigoConvite é igual ao convidado anterior
        convidados.adicionarConvidado("Charlie", 1235);
        convidados.adicionarConvidado("David", 1236);

        // Exibindo o número de convidados
        System.out.println("\nExistem " + convidados.contarConvidados() + " convidado(s) dentro do Set de Convidados");

        // Exibindo os convidados no conjunto
        System.out.println("\nConvidados dentro do Set de Convidados: ");
        convidados.exibirConvidados();

        // Removendo um convidado
        convidados.removerConvidadoPorCodigoConvite(1234);


        // Exibindo os convidados no conjunto
        System.out.println("\nConvidados dentro do Set de Convidados: ");
        convidados.exibirConvidados();

    }
}
