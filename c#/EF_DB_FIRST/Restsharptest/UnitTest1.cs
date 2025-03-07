using Newtonsoft.Json;
using RestSharp;
using System.Net;

namespace Restsharptest
{
    public class Category
    {
        public int CategoryId { get; set; }

        public string CategoryName { get; set; } = null!;

    }
    public class Tests
    {
        private RestClient client;
        private const string BaseUrl = "https://localhost:7180/api/Categories";
        [SetUp]
        public void Setup()
        {
            client = new RestClient(BaseUrl);
        }
        [Test]
        public async Task GetCategories_should_Return_ListOfCategories()
        {
            var request = new RestRequest("/", Method.Get);
            var response = await client.ExecuteAsync(request);

            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
            Assert.IsNotNull(response.Content);

            var categories = JsonConvert.DeserializeObject<List<Category>>(response.Content);
            Assert.IsInstanceOf<List<Category>>(categories);
        }
        [Test]
        public async Task GetCategory_ShouldReturn_WhenValidId()
        {
            var request = new RestRequest("/2", Method.Get);
            var response = await client.ExecuteAsync(request);

            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
            Assert.IsNotNull(response.Content);

            var category = JsonConvert.DeserializeObject<Category>(response.Content);
            Assert.IsNotNull(category);
        }

        [Test]
        public async Task GetCategory_ShouldReturnNotFound_WhenInValidId()
        {
            var request = new RestRequest("/9999", Method.Get);
            var response = await client.ExecuteAsync(request);

            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.NotFound));

        }

        [Test]
        public async Task PostCategory_ShouldCreateCategory()
        {
            var newCategory = new Category() { CategoryName = "test" };
            var request = new RestRequest("/", Method.Post);
            request.AddJsonBody(newCategory);

            var response = await client.ExecuteAsync(request);

            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.Created));
        }

        [Test]
        public async Task PutCategory_ShouldUpdateCategory()
        {
            var updatedCategory = new Category() { CategoryId = 4, CategoryName = "updated Category" };
            var request = new RestRequest("/4", Method.Put);
            request.AddJsonBody(updatedCategory);

            var response = await client.ExecuteAsync(request);

            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.NoContent));
        }

        [Test]
        public async Task DeleteCategroy_ShouldRemoveCategory()
        {
            var request = new RestRequest("/2", Method.Delete);

            var response = await client.ExecuteAsync(request);

            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.NoContent));
        }
        [TearDown]
        public void tearDown()
        {
            client.Dispose();
        }
    }
}