from django.db import models


class Client(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.email
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
         return self.name 

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(product.value for product in self.products.all())
    
    def __str__(self):
        return f'Order {self.id}'