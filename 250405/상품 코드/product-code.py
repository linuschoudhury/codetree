product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product:
    def __init__(self,product_name,product_code):
        self.product_name=product_name
        self.product_code=product_code
product1=Product('codetree',50)
product2=Product(product_name,product_code)


print('product %d is %s'%(product1.product_code,product1.product_name))
print('product %d is %s'%(product2.product_code,product2.product_name))
