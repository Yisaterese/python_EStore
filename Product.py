class Product:
    def __init__(self, product_id:int, product_name:str, price:float, product_description:str, ProductCategory):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.product_description = product_description
        self.productCategory = ProductCategory()