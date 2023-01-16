from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import CreateNewUser


# Create your views here.
def index(response):
    form = CreateNewUser()
    userList = User.objects.all()
    if response.method == "POST":
        form = CreateNewUser(response.POST)

        if form.is_valid():
            u = User(username = form.cleaned_data["username"])
            u.save()
    # user = User.objects.get(id=id)
    return render(response, "main/home.html", {"form":form, "userList":userList})