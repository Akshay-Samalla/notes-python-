using Microsoft.EntityFrameworkCore;
using Repositories.Models;
using System.Collections.Generic;

namespace Repositories.Data
{
    public class AppDbContext: DbContext
    {
        
            public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }


            public DbSet<Product> Products { get; set; }

        
    }
}
