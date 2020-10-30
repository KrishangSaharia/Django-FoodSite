from django.db import models
from django.conf import settings

from django.contrib.auth.models import User


class Transaction(models.Model):
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    date_created=models.DateTimeField('Order Date',auto_now_add=True)
    amount=models.IntegerField(default=100)
    def __str__(self):
        return str(self.id)



class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)


# Create your models here.
