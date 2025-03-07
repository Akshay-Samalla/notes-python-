using EF_CF_multitable.Models;

namespace EF_CF_multitable.Repositories
{
    public interface IProductRepository : IGenericRepository<Product>
    {
        Task<IEnumerable<Product>> SearchProducts(string keyword);
    }
}
