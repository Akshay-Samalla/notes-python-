// See https://aka.ms/new-console-template for more information
using EncapsulationDemo;

Console.WriteLine("Hello, World!");

var account = new BankAccount("12345678", "John Snow", 9000);
account.DisplayAccountInfo();

account.Deposit(10);
account.Withdraw(2000);

try
{
    account.AccountHolder = "";
}
catch (Exception e)
{
    Console.WriteLine($"Error : {e.Message}");
}