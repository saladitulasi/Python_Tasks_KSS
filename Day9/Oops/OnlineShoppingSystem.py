class Product:
    def product_details(self):
        print("Product Name: Smartphone")
        print("Product ID: 101")

class ElectronicProduct(Product):
    def electronic_details(self):
        print("Category: Electronics")
        print("Brand: Samsung")

class MobilePhone(ElectronicProduct):
    def mobile_details(self):
        print("Model: Galaxy S24")
        print("Price: Rs. 50000")

m = MobilePhone()

m.product_details()
m.electronic_details()
m.mobile_details()