from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import UserForm
# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def help(request):
    context_dict = {'help':'Help Page'}
    return render(request,'AppTwo/help.html',context=context_dict)

def users(request):
    users = User.objects.order_by('last_name')
    context_dict = {'users':users}
    return render(request,'AppTwo/users.html',context=context_dict)

def user(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    context_dict = {'user_form':form}
    return render(request,'AppTwo/user.html',context=context_dict)
