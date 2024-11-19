using System;
using ProjetoPOO.Models;


// Instanciando o objeto Iphone
Iphone meuIphone = new Iphone("123456789", "iPhone 14", "ABC123456", 128);
Console.WriteLine("Instalando app no iPhone:");
meuIphone.InstalarAplicativo("Google Play Store");


// Instanciando o objeto Nokia
Nokia meuNokia = new Nokia("987654321", "Nokia 3310", "DEF987654", 64);
Console.WriteLine("\nInstalando app no Nokia:");
meuNokia.InstalarAplicativo("Google Play Store");
