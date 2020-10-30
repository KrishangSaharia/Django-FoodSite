from django import forms

class FeedbackForm(forms.Form):
    message=forms.CharField(max_length=200)
    

