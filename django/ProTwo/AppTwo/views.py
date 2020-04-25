from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    return HttpResponse('Welcome to the index page!')

def help(request):
    context_dict = {'help':'Help Page'}
    return render(request,'AppTwo/help.html',context=context_dict)

def users(request):
    users = User.objects.order_by('last_name')
    context_dict = {'users':users}
    return render(request,'AppTwo/users.html',context=context_dict)
