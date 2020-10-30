from django.db import models



class DeliveryBoy(models.Model):
    name=models.CharField(max_length=100)
    area=models.CharField(max_length=50)
    pincode=models.PositiveIntegerField()
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.name
# Create your models here.
