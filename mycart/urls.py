from django.urls import path
from . import views

app_name='mycart'

urlpatterns=[
        
    path('view/',views.view_cart, name='view_cart'),        
    path('add/<int:item_id>/',views.add_cart, name='add_cart'),    
    path('checkout/',views.checkout, name='checkout'),
        
        
        
        
]
