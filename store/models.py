from django.db import models
import datetime
from djmoney.models.fields import MoneyField  
from django.contrib.auth.models import User

# Categories of products
class Category(models.Model):
    name = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

# Customers    
class Customer(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100) 
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
# All our Products   
class Product (models.Model):
   name = models.CharField(max_length=50) 
   price = MoneyField(max_digits=10 , decimal_places= 2,default=0,default_currency= 'KES')
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   description = models.TextField(max_length=500, default='', blank = True, null=True)
   image = models.ImageField(upload_to = 'Products')
   stock = models.IntegerField(default=0)
#Add sale
   on_sale = models.BooleanField(default=False)
   sale_price = MoneyField(max_digits=10 , decimal_places= 2,default=0,default_currency= 'KES')
   related_products = models.ManyToManyField('self', blank=True)
   def __str__(self):
        return self.name
    
   
class cart(models.Model):
       user =models.OneToOneField(User,on_delete=models.CASCADE)
       
class cartItem(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()       
    
# Customer orders  
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer =models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='',blank=True)
    phone = models.CharField(max_length=20, default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
     return self.product