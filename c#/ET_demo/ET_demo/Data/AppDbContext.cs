
using ET_demo.Models;
using Microsoft.EntityFrameworkCore;

namespace ET_demo.Data
{
    public class AppDbContext:DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }
        public DbSet<Product> Products { get; set; }

    }
}
