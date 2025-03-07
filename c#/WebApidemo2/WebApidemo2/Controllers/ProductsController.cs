using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using WebApidemo2.Models;

namespace WebApidemo2.Controllers
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
        [HttpGet]
        public ActionResult<IEnumerable<Product>> GetAllProducts()
        {
            return products;
        }
        [HttpGet("{id}")]
        public ActionResult<Product> GetProductById(int id)
        {
            var product = products.FirstOrDefault(p => p.Id == id);
            if (product == null)
                return NotFound("The given product id not available");
            return Ok(product);
        }
        [HttpPost]
        public ActionResult<Product> AddNewProduct(Product product)
        {
            product.Id = products.Count + 1;
            products.Add(product);
            return CreatedAtAction(nameof(GetProductById), new { id = product.Id }, product);
        }
        [HttpGet("sample")]

        public string GetSample()
        {
            return "test method";
        }

        [HttpPut("{id}")]
        public ActionResult UpdateProduct(int id, [FromBody] Product updatedProduct)
        {
            var product = products.FirstOrDefault(p => p.Id == id);
            if (product == null)
                return NotFound("Product Not Found");
            product.Name = updatedProduct.Name;
            product.Price = updatedProduct.Price;
            return NoContent();
        }
        [HttpDelete("{id}")]
        public ActionResult DeleteProduct(int id)
        {
            var product = products.FirstOrDefault(p => p.Id == id);
            if (product == null)
                return NotFound("product not found");
            products.Remove(product);
            return NoContent();
        }
    }
}
