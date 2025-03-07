using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Employee
    {
        int empId;
        string name, designation, location;
        double salary;
        public void GetEmployeeInfo()
        {
            Console.WriteLine("Enter the employee id, name , designation" +
                ", location and salary");
            empId = Convert.ToInt32(Console.ReadLine());
            name = Console.ReadLine();
            designation = Console.ReadLine();
            location = Console.ReadLine();
            salary = Convert.ToDouble(Console.ReadLine());


        }
        public void PrintEmployyeInfo()
        {
            Console.WriteLine($"id = {empId} \n name = {name}\n" +
                $"designation = {designation} \n location={location}" +
                $"salary = {salary}");
        }
    }
}
