from django.contrib import admin
from .models import Transaction,Feedback


admin.site.register(Feedback)
admin.site.register(Transaction)

# Register your models here.
