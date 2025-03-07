using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using ET_demo.Models;
using ET_demo.Data;

namespace ET_demo.Controllers
{
    [Route("api/[controller]")]
    [ApiController]

    public class ProductsController : ControllerBase
    {
        private static List<Product> products = new List<Product>()
        {
            new Product{Id=1, Name="Mouse", Price=900},
            new Product{Id=2, Name="Laptop", Price=78000},
            new Product{Id=3, Name="Monitor", Price=4500}
        };
        private readonly AppDbContext _context;


        public ProductsController(AppDbContext context)

        {

            _context = context;


        }

        [HttpGet]

        public ActionResult<IEnumerable<Product>> GetAllProducts()

        {

            return _context.Products.ToList();

        }

        [HttpGet("{id}")]

        public ActionResult<Product> GetProduct(int id)

        {

            var product = _context.Products.Find(id);

            if (product == null)

            {

                return NotFound();

            }

            return product;

        }


        [HttpPost]

        public ActionResult<Product> AddProduct(Product product)

        {

            _context.Products.Add(product);

            _context.SaveChanges();

            return CreatedAtAction(nameof(GetProduct), new { id = product.Id }, product);

        }

        [HttpPut("{id}")]

        public ActionResult UpdateProduct(int id, [FromBody] Product updatedProduct)

        {

            var product = _context.Products.Find(id);

            if (product == null)

                return NotFound("Product not found");


            product.Name = updatedProduct.Name;

            product.Price = updatedProduct.Price;


            _context.SaveChangesAsync();

            return NoContent();

        }

        [HttpDelete("{id}")]

        public ActionResult DeleteProduct(int id)

        {

            var product = _context.Products.Find(id);

            if (product == null)

                return NotFound("Product not found");


            _context.Products.Remove(product);

            _context.SaveChanges();

            return NoContent();

        }
    }
}
