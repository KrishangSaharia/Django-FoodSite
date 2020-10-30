from django.db import models
from django.conf import settings 
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Offer(models.Model):
    message=models.CharField(max_length=300)
    coupon_code=models.CharField(blank=True, max_length=40)
    subject=models.CharField(max_length=75)

    def __str__(self):
        return self.subject


@receiver(post_save, sender= Offer)
def send_tracking_email(sender, instance, **kwargs):
    send_mail(
        subject='Bumper Offer',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['krishangsaharia2@gmail.com'],
        message='Welcome to the world oF Offers and Discounts'
                )


# Create your models here.
