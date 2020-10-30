from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import Transaction
from .models import Feedback
from .forms import FeedbackForm
from django.utils  import timezone

def new(request):
    user=request.user
    transaction=Transaction.objects.create(user=user)
    transaction.save()
    return HttpResponseRedirect("thanks/")




def thanks(request):
    return render(request,'transaction/thanks.html', {})





def view(request):
    user=request.user
    transactions=user.transaction_set.all()
    return render(request,'transaction/view.html',{'transactions':transactions})



def feedback(request,transactionid):
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            message=form.cleaned_data['message']
            user=request.user
            transaction=Transaction.objects.get(pk=transactionid)
            feedback=Feedback(user=user, transaction=transaction,message=message, timestamp=timezone.now())
            feedback.save()
            return HttpResponseRedirect(reverse('home:main'))

    else:
        form=FeedbackForm()
    return render(request,'transaction/feedback.html', {'form':form,'transactionid':transactionid})

# Create your views here.
