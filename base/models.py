from django.db import models

# Create your models here.

class Product(models.Model):
    item=models.CharField(max_length=50,null=True,blank=True)
    desc = models.CharField(max_length=256,null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['item','desc','price']
 
    def __str__(self):
           return self.desc
