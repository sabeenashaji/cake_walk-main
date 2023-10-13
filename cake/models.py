from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    

class Cake(models.Model):
    cake_name = models.CharField( max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to="item_image",null=True,blank=True)
    image1 = models.ImageField(upload_to="item_image",null=True,blank=True)
    image2 = models.ImageField(upload_to="item_image",null=True,blank=True)
    image3 = models.ImageField(upload_to="item_image",null=True,blank=True)
    
    def __str__(self):
        return self.cake_name
    

class Profile(models.Model):
    name=models.CharField(max_length=100)
    fullname=models.CharField(max_length=100)
    emailaddress=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    location=models.CharField(max_length=100)
    pincode=models.IntegerField()

    def __str__(self):
        return self.fullname

class SignUp(models.Model):
    fullname=models.CharField(max_length=100)
    emailaddress=models.CharField(max_length=100)
    phonenumber=models.CharField( max_length=12)
    location=models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname