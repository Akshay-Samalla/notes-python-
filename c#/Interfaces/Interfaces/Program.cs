// See https://aka.ms/new-console-template for more information
using Interfaces;

Console.WriteLine("Hello, World!");
Developer developer = new Developer("tina", 23, 1232);
developer.DoWork();
Tester tester = new Tester();
tester.DoWork();
Mananger manager = new Mananger("rome", 34, 213);
manager.DisplayInfo();
manager.DoWork();
manager.Manage();