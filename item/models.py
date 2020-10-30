from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not a non-negetive  number'),
            params={'value': value},
        )

CATEGORIES=(
        
        
        ("South Indian","South Indian"),
        ("Italian", "Italian"),
        ("Mexican","Mexican"),
        ("Chinese","Chinese"),
        ("North Indian","North Indian"),
        
)



class Item(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(validators=[validate_positive])
    is_available=models.BooleanField(default=True)
    category=models.CharField(choices=CATEGORIES,default='North Indian',max_length=100)
    photo=models.ImageField(upload_to="gallery")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Combo(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(validators=[validate_positive])
    description=models.CharField(max_length=200)
    is_available=models.BooleanField(default=True)
    photo=models.ImageField(upload_to="gallery")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
# Create your models here.
