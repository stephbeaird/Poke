from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . models import User
# from . models i

# Create your views here.
def index(request):
    return render(request, "users/index.html")

def register(request):
    return redirect('/main')

def login(request):
    return redirect('users/main.html')

def main(request):
    return render(request, 'users/main.html')

def logout(request):
    return redirect('/')


def update(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/index' + id)
    else: 
        users = Users.objects.get(id = id)
        users.name = request.POST['name']
        users.desc = request.POST['desc']
        users.save()
        return redirect('/users')
