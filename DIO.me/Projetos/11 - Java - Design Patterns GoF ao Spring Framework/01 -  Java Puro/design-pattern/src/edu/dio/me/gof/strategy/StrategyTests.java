package edu.dio.me.gof.strategy;

public class StrategyTests {

    public static void main(String[] args) {
        
        // Testes relacionados ao Design Pattern Strategy
        Robo robo = new Robo();

        Comportamento normal = new ComportamentoNormal();
        Comportamento defensivo = new ComportamentoDefensivo();
        Comportamento agressivo = new ComportamentoAgressivo();

        robo.setStrategy(normal);
        robo.mover();

        robo.setStrategy(defensivo);
        robo.mover();

        robo.setStrategy(agressivo);
        robo.mover();
    }
}
