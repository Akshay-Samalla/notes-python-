using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Interfaces.interfaces;

namespace Interfaces
{
    internal class Person
    {
        protected string Name { get; set; }
        protected int Age { get; set; }
        public Person(string name, int age)
        {
            Name = name;Age = age;
        }
        public virtual void DisplayInfo()
        {
            Console.WriteLine($"name:{Name},age:{Age}");
        }
    }
    internal class Student(int id, string domain)
    {
        public int StudentId { get; } = id;
        public string Domain { get; } = domain;
        public virtual void DisplayStudentInfo()
        {
            Console.WriteLine($"student id ={StudentId}, domain = {Domain}");
        }
    }
    class Developer : IWork
    {
        public Developer(string name,int age, int empid)
        { }
        public void DoWork()
        {
            Console.WriteLine("developer is writing the code");
        }
    }
    class Tester:IWork
    {
        public void DoWork()
        {
            Console.WriteLine("tester is testing the code or performance of an application");
        }
    }
    class Mananger : Person, IWork, IManage
    {
        public object EmpId { get; private set; }

        public Mananger(string name, int age, int EmpId) : base(name, age)
        {
           
        }

        public void DoWork()
        {
            Console.WriteLine("manager is coordinating with the client");

        }

        public void Manage()
        {
            Console.WriteLine("managers the team");
        }
        public override void  DisplayInfo()
        {
            base.DisplayInfo();
            Console.WriteLine($"employee ID :{EmpId}");
        }
    }

}
