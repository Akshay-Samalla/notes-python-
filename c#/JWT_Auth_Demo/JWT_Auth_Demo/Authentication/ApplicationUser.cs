
using Microsoft.AspNetCore.Identity;

namespace JWT_Auth_Demo.Authentication
{
    public class ApplicationUser : IdentityUser
    {
        public string FirstName { get; set; }

        public string LastName { get; set; }

        public DateTime DateOfBirth { get; set; }
    }
}
