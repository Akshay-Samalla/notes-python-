using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace AzurePublishDemo.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class HelloController : ControllerBase
    {
        [HttpGet]
        public string Index()
        {
            return "hello welcome to azure";
        }
    }
}
