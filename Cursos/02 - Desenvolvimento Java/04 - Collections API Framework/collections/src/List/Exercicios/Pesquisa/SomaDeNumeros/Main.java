// ├───┬───> Exercício: Soma de Números
// │   │
// │   └───>    Crie uma classe chamada "SomaNumeros" que possui uma lista de números inteiros como atributo.
// │        Implemente os seguintes métodos:
// │
// │            * adicionarNumero(int numero): Adiciona um número à lista de números.
// │            * calcularSoma(): Calcula a soma de todos os números na lista e retorna o resultado.
// │            * encontrarMaiorNumero(): Encontra o maior número na lista e retorna o valor.
// │            * encontrarMenorNumero(): Encontra o menor número na lista e retorna o valor.
// │            * exibirNumeros(): Retorna uma lista contendo todos os números presentes na lista.
// │
// │
// │
// └───────> Código:

package List.Exercicios.Pesquisa.SomaDeNumeros;

public class Main {
    public static void main(String[] args) {

        // Instânciando um objeto da classe 'SomaDeNumeros'
        SomaDeNumeros somaDeNumeros = new SomaDeNumeros();

        // Adicionando numeros à 'somaDeNumeros'
        somaDeNumeros.adicionarNumero(2);
        somaDeNumeros.adicionarNumero(22);
        somaDeNumeros.adicionarNumero(222);

        // Encontrando o maior número em 'somaDeNumeros'
        int maiorNumero = somaDeNumeros.encontrarMaiorNumero();
        System.out.println("O maior número da lista é: " + maiorNumero);
        
        // Encontrando o menor número em 'somaDeNumeros'
        int menorNumero = somaDeNumeros.encontrarMenorNumero();
        System.out.println("O menor número da lista é: " + menorNumero);

        // Calculando a soma total entre os números em 'somaDeNumeros'
        int soma = somaDeNumeros.calcularSoma();
        System.out.println("A soma total da lista é: " + soma);
    }
}
