using Microsoft.AspNetCore.Mvc;
using ProductApi.Models;

namespace ProductApi.Controllers;

[ApiController]
[Route("[controller]")]
public class ProductController : ControllerBase
{
    public static List<Product> products = new List<Product>();
    public ProductController()
    {
        if(products.Count==0)
        {
            products.Add(new Product { Id = 1, Name = "product 1", Description = "description 1", Category = "category 1", Price = 1234 });
            products.Add(new Product { Id = 2, Name = "product 2", Description = "description 2", Category = "category 2", Price = 321 });
            products.Add(new Product { Id = 3, Name = "product 3", Description = "description 3", Category = "category 3", Price = 456 });
            products.Add(new Product { Id = 4, Name = "product 4", Description = "description 4", Category = "category 4", Price = 123});
        }
    }
    [HttpGet]
    public List<Product> Get()
    {
        return products;
    }
    [HttpPut]
    public string UpdateProduct(Product product)
    {
        Product foundproduct = products.Find(p => p.Id == product.Id);
        if (foundproduct != null)
        {
            foundproduct.Name = product.Name;
            foundproduct.Description = product.Description;
            foundproduct.Category = product.Category;
            foundproduct.Price = product.Price;
            return "Updated";


        }
        else
        {
            return "Sorry! Record Not Updated";

        }
    }
    [HttpPost]
    public string AddNewProduct(Product product)
    {
        products.Add(product);
        return product.Name;
    }

    [HttpDelete]
    public string RemoveProduct(Product product)
    {
        Product foundProduct = products.Find(p => p.Id == product.Id);
        if (foundProduct != null)
        {
            products.Remove(foundProduct);
            return "product removed";
        }
        else
        {
            return "product not available";
        }
    }
}
