using Microsoft.EntityFrameworkCore;
using Repositories.Data;
using Repositories.Models;

namespace Repositories.Repos
{
    public class ProductRepository:IProductRepository
    {
        private readonly AppDbContext _context;
        public ProductRepository(AppDbContext context)
        {
            _context = context;
        }
        

        public async Task<IEnumerable<Product>> GetProductsAsync()

        {

            return await _context.Products.ToListAsync();

        }


        public async Task<Product> GetProductByIdAsync(int id)

        {

            return await _context.Products.FindAsync(id);

        }


        public async Task<Product> AddProductAsync(Product product)

        {

            _context.Products.Add(product);

            await _context.SaveChangesAsync();

            return product;

        }


        public async Task<Product> UpdateProductAsync(int id, Product product)

        {

            var updateProduct = await _context.Products.FindAsync(id);

            if (updateProduct == null)

            {

                return null; // Return null if product not found

            }


            updateProduct.Name = product.Name;

            updateProduct.Price = product.Price;


            await _context.SaveChangesAsync();

            return updateProduct; // Return updated product

        }


        public async Task<string> DeleteProductAsync(int id)

        {

            var prodcut = await _context.Products.FindAsync(id);

            if (prodcut != null)

            {

                _context.Remove(prodcut);

                await _context.SaveChangesAsync();

                return "Product Removed Successfully";

            }

            else

                return "Product not found";

        }

    }
}
