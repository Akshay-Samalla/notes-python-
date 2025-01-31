'''


7) Calculate Discounts for Products
 You have a list of products with their prices. Apply a 20% discount to products costing more than $100 and return the updated prices.

	products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
   ]
list out discounted products

'''

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
   ]
products=map(lambda x: {'name':x['name'],'price':x['price']*0.8} if x['price']>100 else x , products)
products=list(products)
print('updated products ', products)
print('discounted products')
products=filter(lambda x: x['price']>100 , products)
print(list(products))





