using OpenQA.Selenium.Support.UI;
using OpenQA.Selenium;
using SeleniumExtras.WaitHelpers;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DotnetSeliniumTest
{
    public class SeleniumHelper
    {
        private readonly IWebDriver driver;
        private readonly WebDriverWait _wait;

        public SeleniumHelper(IWebDriver driver, int timeoutInSeconds = 10)
        {
            this.driver = driver;
            _wait = new WebDriverWait(driver, TimeSpan.FromSeconds(timeoutInSeconds));
        }


        public void NavigateUrl(string url)
        {
            driver.Navigate().GoToUrl(url);
        }
      
        public void ClickElement(By locator)
        {
            _wait.Until(ExpectedConditions.ElementToBeClickable(locator)).Click();
        }


        public void EnterText(By locator, string text)
        {
            var element = _wait.Until(ExpectedConditions.ElementIsVisible(locator));
            element.Clear();
            element.SendKeys(text);
        }

        public void WaitForElement(By locator)
        {
            _wait.Until(ExpectedConditions.ElementExists(locator));
        }

        public bool IsElementDisplayed(By locator)
        {
            try
            {
                return driver.FindElement(locator).Displayed;
            }
            catch (NoSuchElementException)
            {
                return false;
            }
        }
    
}
}
