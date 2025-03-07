using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CalcuationLibrary
{
    public class Calculator
    {
        int num1, num2, addition, difference, product;
        public void getNumbers()
        {
            Console.WriteLine("enter the value for the num1 and num2");
            num1 = Convert.ToInt32(Console.ReadLine());
            num2 = Convert.ToInt32(Console.ReadLine());
        }
        public void Addition()
        {
            addition = num1 + num2;
            Console.WriteLine("addtion "+addition);
        }
        public void Subtration()
        {
            difference = num1 - num2;
            Console.WriteLine("subtraction"+difference);
        }
        public void Multiplication()
        {
            product = num1 * num2;
            Console.WriteLine("multiplication"+product);
        }
    }
}
