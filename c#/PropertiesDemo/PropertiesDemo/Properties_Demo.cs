using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PropertiesDemo
{
    class Properties_Demo
    {
        private string _accountNubmer = "3456";
        public string accountNumber
        {
            get => _accountNubmer;
            set => _accountNubmer = value;
        }
    }
}
