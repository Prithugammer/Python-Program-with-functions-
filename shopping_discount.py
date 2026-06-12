from discount import final_price , Tax_Rate

products = ['laptop',85000,10,'Headphones',4500,15,'Phone Case',800,5,
            'USB Cable',600,0]

for i in range(0,len(products),3):
    price = final_price(products[i+1],products[i+2])

    print(f'{products[i]}  Original price : {products[i+1]} Final price : {price}')

print(f'Tax Rate is {Tax_Rate}')