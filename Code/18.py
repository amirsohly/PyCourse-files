class Product :
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}({self.price})"
    
p1 = Product("Mercedes Benz C300", 62000)
p2 = Product("BMW M5", 90000)
print(p1)
print(p2)