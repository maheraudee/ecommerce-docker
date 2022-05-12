from multiprocessing import context
from tkinter import Menu
from django.shortcuts import render

from .form import ApplyForm

from .models import Item,Menu,Order,Customer,Worker,Person
# Create your views here.


def about(request):
    return render(request,"cafe/about.html")
def home(request):
    return render(request,"cafe/home.html")
def reservation(request):
    
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            myform = form.save()
    else:
        form = ApplyForm()

    context = {'form': form}

    return render(request,"cafe/reservation.html",context)
def team(request):
    workers = Worker.objects.all()
    context={
        'workers': workers
    }
    return render(request,"cafe/team.html", context)


def special_dishes(request):
    return render(request,"cafe/special-dishes.html")


def menu(request):
    # items = Item.objects.all()
    # menus = Menu.objects.search(code='Breakfast')
    
    menus = Menu.objects.all()
    context={
    'menus': menus
    }
    
    return render(request,"cafe/menu.html",context)