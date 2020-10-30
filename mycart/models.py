from django.db import models
from datetime import datetime
from django.utils import timezone

from item.models import Item
from django.conf import settings
from item.models import Item

User=settings.AUTH_USER_MODEL

class Cart(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    items=models.ManyToManyField(Item,blank=True)
    total=models.DecimalField(default=0.00, max_digits=100,decimal_places=2)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    item=models.ForeignKey( Item,null=True,blank=True,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,null=True,blank=True,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)



    









# Create your models here.
