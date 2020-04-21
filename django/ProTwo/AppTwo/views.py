from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Welcome to the index page!')

def help(request):
    context_dict = {'help':'Help Page'}
    return render(request,'AppTwo/help.html',context=context_dict)
