from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):

    your_name = forms.CharField(widget=forms.TextInput(
        attrs={'size': '48', 'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'size': '48', 'class': 'form-control', 'placeholder': 'Email Address'}))
    details = forms.CharField(widget=forms.Textarea(
        attrs={'size': '48', 'class': 'form-control', 'placeholder': 'Please leave your Message'}))

    class Meta:
        model=Feedback
        fields=('your_name','email','details')
