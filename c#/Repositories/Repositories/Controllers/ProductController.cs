using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Repositories.Data;
using Repositories.Models;
using static Repositories.Data.AppDbContext;

namespace Repositories.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductController : ControllerBase
    {
        private readonly AppDbContext _context;


        public ProductController(AppDbContext context)

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
