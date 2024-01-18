from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Shoes(models.Model):
    brand=models.CharField(max_length=250)
    gender=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale=models.CharField(max_length=10)
    image=models.ImageField(upload_to='gallery')
    image2=models.ImageField(upload_to='gallery')
    image3=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    product = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'