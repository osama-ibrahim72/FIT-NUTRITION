from re import X
from unicodedata import category
from django.shortcuts import render
#from sympy import re
from .models import Food3
from .models import Workout3
#from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')

def calc(request):
    return render(request, 'pages/calc.html')

def foods(request):
    return render(request,'pages/foods.html',{'foo':Food3.objects.all()})

def workouts(request):
    return render(request,'pages/workouts.html',)

def legworkouts(request):
    return render(request,'pages/legs.html',{'woo':Workout3.objects.filter(category='legs')})

def backworkouts(request):
    return render(request,'pages/back.html',{'woo':Workout3.objects.filter(category='back')})

def chestworkouts(request):
    return render(request,'pages/chest.html',{'woo':Workout3.objects.filter(category='chest')})

def armworkouts(request):
    return render(request,'pages/arm.html',{'woo':Workout3.objects.filter(category='arm')})

def shoulderworkouts(request):
    return render(request,'pages/shoulder.html',{'woo':Workout3.objects.filter(category='shoulder')})



