from django.db import models

from  cake.models import Profile,Cake
from django.utils import timezone


# Create your models here



class Cart(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)



class CartItem(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE) 
    quantity=models.PositiveIntegerField(default=0)  


    def __str__(self):
        return f"CartItem for {self.user.fullname}" 