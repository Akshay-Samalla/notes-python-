using RestSharp;
using System.Net;

namespace RestSharpapitestproject;
public class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public decimal Price { get; set; }

    }
public class ProductApITest
{
    
    private RestClient client;
    private const string BaseUrl = "https://localhost:7161/Product";

    [SetUp]
    public void Setup()
    {
        client = new RestClient(BaseUrl);

    }

    [Test]
    public async Task Test_AddProduct()
    {
        var request = new RestRequest("/", Method.Post);
        request.AddJsonBody(new
        {
            Id = 1,
            Name = "Product 5",
            Description = "Description 5",
            Category = "Category 5",
            Price = 500
        });

        var response = await client.ExecuteAsync(request);
        Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
        Assert.That(response.Content, Does.Contain("Product 5"));
    }
    [Test]
    public async Task TestGetAllProducts()
    {
        var request = new RestRequest("/", Method.Get);
        var response = await client.ExecuteAsync<List<Product>>(request);
        Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
        Assert.IsNotNull(response.Data);
        Assert.That(response.Data.Count, Is.GreaterThan(0));
    }
    [Test]
    public async Task Test_update()
    {
        var request = new RestRequest("/",Method.Put);
        request.AddJsonBody(new
        {
            Id = 1,
            Name = " update Product 5",
            Description = "update Description 5",
            Category = "updateCategory 5",
            Price = 500
        });

        var response = await client.ExecuteAsync(request);
        Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
        Assert.That(response.Content, Does.Contain("Updated"));
    }
    [Test]
    public async Task Test_delete()
    {
        var request = new RestRequest("/", Method.Delete);
        request.AddJsonBody(new
        {
            Id = 5,
            Name = "Product 5",
            Description = "Description 5",
            Category = "Category 5",
            Price = 500
        });

        var response = await client.ExecuteAsync(request);
        Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
        Assert.That(response.Content, Does.Contain("product removed"));
    }

    [TearDown]
    public void TearDown()
    {
        client.Dispose();
    }
}


