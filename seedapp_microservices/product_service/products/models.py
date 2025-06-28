from django.db import models
import uuid
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    available = models.BooleanField(default=True)                  
    
    def __str__(self):
        return self.name
    
    def get_image_url(self):
        if self.image:
            return self.image.url and self.name
        return None
    

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('Advance', 'Advance'),
        ('Full', 'Full Payment')]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    buyer_contact = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=1)
    payment_option = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='Advance') 

    def __str__(self):
        return self.product.name
