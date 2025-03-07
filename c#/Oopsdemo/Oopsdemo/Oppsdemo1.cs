using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oopsdemo
{
    internal class Sample
    {
        string name = "";
        public Sample()
        {
            Console.WriteLine("i am default constructor");
        }
        public Sample(string companyName)
        {
            Console.WriteLine("parmeterised constructor");
            name = companyName;
            Console.WriteLine(companyName);
        }
        public Sample(Sample sampleobj)
        {
            Console.WriteLine("this is copy construcotor");
            Console.WriteLine(sampleobj.name);
        }
        public void Demo()
        {
            Console.WriteLine('demo function');
        }
    }
}
