from django.urls import path
from . import views
app_name='home'

urlpatterns=[
        
        path('<str:item_type>',views.main,name='main'),
        path('',views.main,name='main'),
    
            
]
