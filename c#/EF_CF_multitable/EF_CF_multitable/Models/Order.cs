using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace EF_CF_multitable.Models
{
    public class Order
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public int ProductId { get; set; }
        [ForeignKey("ProductId")]
        public Product Product { get; set; }
        [Required]
        public int Qantity { get; set; }
        [Required]
        public decimal TotalPrice { get; set; }
        [Required]
        public DateTime OrderDate { get; set; }
    }
}
