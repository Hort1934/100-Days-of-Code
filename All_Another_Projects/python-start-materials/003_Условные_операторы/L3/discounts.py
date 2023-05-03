product_price = 350
if product_price > 1000:
    product_price = product_price * (1 - 0.1)
elif product_price > 500:
    product_price = product_price * (1 - 0.05)
elif product_price > 100:
    product_price = product_price * (1 - 0.03)
print(product_price)
