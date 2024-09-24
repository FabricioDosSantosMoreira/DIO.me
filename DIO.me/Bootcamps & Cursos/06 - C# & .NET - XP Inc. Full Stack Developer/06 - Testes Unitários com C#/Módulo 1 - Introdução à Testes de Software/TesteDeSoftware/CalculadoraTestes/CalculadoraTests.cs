using Calculadora.Services;

namespace CalculadoraTestes;

// Executando os testes: 
//     dotnet test

// Executando um teste: 
//     dotnet test --filter CalculadoraTests.DeveSomarCincoComDezComRetornoQuinze

// Listando os testes: 
//     dotnet test -t

public class CalculadoraTests
{
    private readonly CalculadoraImpl _calculadora;
    
    public CalculadoraTests()
    {
        _calculadora = new CalculadoraImpl();
    }

    [Fact]
    public void DeveSomarCincoComDezERetornarQuinze()
    {
        // Arrange
        int num1 = 5;
        int num2 = 10;

        // Act
        int resultado = _calculadora.Somar(num1, num2);

        // Assert
        Assert.Equal(15, resultado);
    }

    [Fact]
    public void DeveSomarDezComDezERetornarVinte()
    {
        int num1 = 10;
        int num2 = 10;

        int resultado = _calculadora.Somar(num1, num2);

        Assert.Equal(20, resultado);
    }

    [Fact]
    public void DeveSubtrairDezComCincoERetornarCinco()
    {
        int num1 = 10;
        int num2 = 5;

        int resultado = _calculadora.Subtrair(num1, num2);

        Assert.Equal(5, resultado);
    }  

    [Fact]
    public void DeveMultiplicarDezComCincoERetornarCinquenta()
    {
        int num1 = 10;
        int num2 = 5;

        int resultado = _calculadora.Multiplicar(num1, num2);

        Assert.Equal(50, resultado);
    }  

    [Fact]
    public void DeveDividirDezComCincoERetornarDois()
    {
        int num1 = 10;
        int num2 = 5;

        int resultado = _calculadora.Dividir(num1, num2);

        Assert.Equal(2, resultado);
    }  

    [Fact]
    public void DeveVerificarSeSeteEhParERetornarFalso()
    {
        int num = 7;

        bool resultado = _calculadora.EhPar(num);

        Assert.False(resultado);
    }

    [Fact]
    public void DeveVerificarSeQuatroEhParERetornarVerdadeiro()
    {
        int num = 4;

        bool resultado = _calculadora.EhPar(num);

        Assert.True(resultado);
    }

    [Theory]
    [InlineData(2)] 
    [InlineData(4)] 
    [InlineData(6)] 
    [InlineData(8)] 
    [InlineData(10)]
    public void DeveVerificarSeOsNumerosSaoParesERetornarVerdadeiro(int num)
    {
        bool resultado = _calculadora.EhPar(num);

        Assert.True(resultado);
    }

    [Theory]
    [InlineData(new int[] { 3, 5, 7, 9, 11, 13 })] 
    [InlineData(new int[] { 101, 133, 59679 })] 
    public void DeveVerificarSeOsNumerosSaoParesERetornarFalse(int[] nums)
    {
        Assert.All(nums, num => Assert.False(_calculadora.EhPar(num)));
    }
}