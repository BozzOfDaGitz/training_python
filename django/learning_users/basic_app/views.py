from django.shortcuts import render
from basic_app import forms

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    user_form = forms.UserForm()
    profile_form = forms.UserProfileInfoForm()
    context_dict = {'user_form':user_form,'profile_form':profile_form,'registered':False}
    return render(request,'basic_app/register.html',context=context_dict)