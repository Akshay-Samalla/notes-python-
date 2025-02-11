'''

1) convert the prices in USD & Euro using appropriate function
    PricesList_inr =[3000,56000,45000,2300]


'''
def inr_to_EURO(price_list):
    return list(map(lambda x:x*0.011 , price_list))
def inr_to_USD(price_list):
    return list(map(lambda x:x*0.012 , price_list))

PricesList_inr =[3000,56000,45000,2300]
print(inr_to_EURO(PricesList_inr))
print(inr_to_USD(PricesList_inr))

