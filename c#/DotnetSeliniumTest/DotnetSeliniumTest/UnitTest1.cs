using OpenQA.Selenium.Chrome;
using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using DotnetSeliniumTest.pages;
namespace DotnetSeliniumTest
{
    public class Tests
    {
        private  IWebDriver driver;
        private SeleniumHelper helper;
        [SetUp]
        public void Setup()
        {
            driver = new ChromeDriver();
            helper = new SeleniumHelper(driver);
        }

        [Test]
        public void Test1()
        {
            driver.Navigate().GoToUrl("https://www.google.com/");
            driver.Manage().Window.Maximize();
            IWebElement webElement = driver.FindElement(By.Name("q"));
            webElement.SendKeys("Selenium");
            webElement.SendKeys(Keys.Return);
        }
        [Test]
        public void EAWebsiteTest()
        {
           
            IWebDriver driver = new ChromeDriver();
            driver.Navigate().GoToUrl("http://eaapp.somee.com/");
            IWebElement loginLink = driver.FindElement(By.Id("loginLink"));
            loginLink.Click();
            IWebElement txtUsername = driver.FindElement(By.Id("UserName"));
            txtUsername.SendKeys("admin");
            IWebElement txtPassword = driver.FindElement(By.Id("Password"));
            txtPassword.SendKeys("password");
            IWebElement btnLogin = driver.FindElement(By.Id("loginIn"));
            btnLogin.Click();
            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
            wait.Until(SeleniumExtras.WaitHelpers.ExpectedConditions.ElementExists(By.TagName("img")));                
            try
            {
                IWebElement imageElement = driver.FindElement(By.CssSelector("img[src='/Image/EA_banner_white_v1.jpg']"));
                Assert.IsTrue(imageElement.Displayed, "Image is displayed on the page.");
                Console.WriteLine("Image is present on the page.");
                
            }
            catch (NoSuchElementException)
            {
                Assert.Fail("Image not found on the page.");
            }
            
        }


        [Test]
        public void LoginAndVerifyImage()
        {
            helper.NavigateUrl("http://eaapp.somee.com");
            helper.ClickElement(By.Id("loginLink"));

            helper.EnterText(By.Id("UserName"), "admin");
            helper.EnterText(By.Id("Password"), "password");

            helper.ClickElement(By.Id("loginIn"));

            helper.WaitForElement(By.TagName("img"));
       bool isImageDisplayed = helper.IsElementDisplayed(By.CssSelector("img[src='/Image/EA_banner_white_v1.jpg']"));
            Assert.IsTrue(isImageDisplayed, "Image is displayed on the page.");


        }
        [Test]
        public void WorkingWithAdvancedControls()

        {


            //IWebDriver driver = new ChromeDriver();

            //driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(2);


            driver.Navigate().GoToUrl("C:/Users/aksha/Desktop/New%20folder%20(2)/c%23/DotnetSeliniumTest/DotnetSeliniumTest/Testpage.html");

            FormHelper.EnterText(driver.FindElement(By.Id("name")), "Geetha Eswaramurthi");


            FormHelper.EnterText(driver.FindElement(By.Id("email")), "geethaeswaramurthi@outlook.com");

            FormHelper.EnterText(driver.FindElement(By.Id("doj")), "8-3-2020");

            FormHelper.Click(driver.FindElement(By.CssSelector("input[name='gender'][value='female']")));


            FormHelper.SelectDropDownByText(driver.FindElement(By.Id("city")), "Coimbatore");

            FormHelper.EnterText(driver.FindElement(By.Id("designation")), "Senior Product Engineer");


            FormHelper.MultiSelectElements(driver.FindElement(By.Id("skills")), ["testing", "cloud"]);

            var getSelectedOptions = FormHelper.GetAllSelectedLists(driver.FindElement(By.Id("skills")));


            getSelectedOptions.ForEach(Console.WriteLine);

            FormHelper.Click(driver.FindElement(By.CssSelector("input[name='hobbies'][value='Reading Books']")));

            FormHelper.Click(driver.FindElement(By.CssSelector("input[name='hobbies'][value='Playing Baseball']")));

            var getSelectedHobbies = FormHelper.GetAllCheckedCheckboxes(driver,By.Name("hobbies"));

            getSelectedHobbies.ForEach(Console.WriteLine);

            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(2);

            // Clicking the Register Button

            FormHelper.Click(driver.FindElement(By.CssSelector("button[type='submit']")));


            // Validation: Ensure form submission redirects to a success page or displays a confirmation message

            Thread.Sleep(2000); // Wait for form submission response

            bool isSubmissionSuccessful = driver.PageSource.Contains("Thank you for registering") || driver.Url.Contains("success");

            Assert.IsTrue(isSubmissionSuccessful, "Form submission failed.");



        }

        [Test]
        public void workingwithPOM()
        {            
            driver.Navigate().GoToUrl("http://eaapp.somee.com");
            var pom = new LoginPage(driver);
            pom.ClickLogin();
            pom.login("admin", "password");
            
        }

        [TearDown]
        public void TearDown()
        {
            driver.Quit();
            driver.Dispose();
        }
    }
}