from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse
from item.models import Item,Combo




def main(request,item_type='All'):
     
    if request.method=="GET":
        if item_type=="All" or item_type=="":
            items=Item.objects.all()
        elif item_type=="Italian":
            items=Item.objects.filter(category="Italian")
        elif item_type=="Mexican":
            items=Item.objects.filter(category="Mexican")
        elif item_type=="Chinese":
            items=Item.objects.filter(category="Chinese")
        elif item_type=="North Indian":
            items=Item.objects.filter(category="North Indian")
        elif item_type=="South Indian":
            items=Item.objects.filter(category="South Indian")
        elif item_type=="Combo":
            items=Combo.objects.all()
        user=request.user 
    return render(request,'home/main.html',{'items':items,'item_type':item_type,'authenticated_user':user.is_authenticated})



 #Create  your views here.
