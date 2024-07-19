package edu.me.gof.singleton;

public class SingletonTests {

    public static void main(String[] args) {
        
        // Testes relacionados ao Design Pattern Singleton
        System.out.println("\nSingleton Lazy:");
        SingletonLazy lazy = SingletonLazy.getInstancia();
        System.out.println(lazy);

        lazy = SingletonLazy.getInstancia();
        System.out.println(lazy);


        System.out.println("\nSingleton Eager:");
        SingletonEager eager = SingletonEager.getInstancia();
        System.out.println(eager);

        eager = SingletonEager.getInstancia();
        System.out.println(eager);


        System.out.println("\nSingleton Lazy Holder:");
        SingletonLazyHolder lazy_holder = SingletonLazyHolder.getInstancia();
        System.out.println(lazy_holder);

        lazy_holder = SingletonLazyHolder.getInstancia();
        System.out.println(lazy_holder);
    }
}
