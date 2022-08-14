
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name
    #user=models.OneToOneField(User,on_delete=models.CASCADE)
    seller_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    desc=models.CharField(max_length=100)
    image =models.ImageField(blank=True,upload_to='images')


   
class OrderDetail(models.Model):
    customer_username = models.CharField(max_length=200)
    product = models.ForeignKey(to='Product',on_delete=models.PROTECT)
    amount = models.IntegerField()
    payment_PUBLISHABLE_KEY= models.CharField(max_length=200)
    payment_KEY = models.CharField(max_length=200)
    # has_paid = models.BooleanField(default=False)
    # created_on = models.DateTimeField(auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now_add=True)
    