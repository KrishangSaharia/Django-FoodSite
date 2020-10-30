from django.urls import path
from . import views


app_name='transaction'



urlpatterns=[
        
    path('new',views.new,name='new'),        
    path('thanks/', views.thanks, name='thanks'),
    path('view/',views.view,name='view'),    
    path('<int:transactionid>/feedback/',views.feedback,name='feedback'),    
        
        
]
