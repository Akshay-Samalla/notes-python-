using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EncapsulationDemo
{
    class BankAccount
    {
        private readonly string _accountNumber;
        private string _accountHolder;
        private decimal _balance;
        public BankAccount(string accountNumber, string accountHolder, decimal initialBalance)
        {
            _accountNumber = accountNumber;
            _accountHolder = accountHolder;
            _balance = initialBalance > 0 ? initialBalance : initialBalance:throw new ArgumentException("zero balance") ;
        }
        //encapsulated property with validations
        public string AccountHolder
        {
            get => _accountHolder;
            set
            {
                if(string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException('account holder cannot be empty')
               _accountHolder = value;
            }
        }
        //read-only property
        public string AccountNumber => _accountNumber

        //read-only balance
        public decimal Balance => _balance;
        //encapuslated method for deposit
        public void Deposit(decimal amount)
        {
            if(amount <=0)
            {
                throw new ArgumentException('deposit amount must be positive');
            }
            _balance += amount;
            Console.WriteLine($"deposited : {amount:C}" +
                $"new balance: {_balance:C}");
        }
        public bool Withdraw(decimal amount)
        {
            if (amount <= 0)
                throw new ArgumentException("withdrawl amount must be positive");
            if (amount > _balance)
            {
                Console.WriteLine("insufficient balance");
                return false;
            }
            _balance -= amount;
            Console.WriteLine($"withdrawn : {amount:C} remainig balance:{_balance:C}");
            return true;
        }
        public void DisplayAccountInfo()
        {
            Console.WriteLine($"accountNumber:{AccountNumber}" +
                $"hoder:{AccountHolder} balance:{Balance}");
        }

    }
}
