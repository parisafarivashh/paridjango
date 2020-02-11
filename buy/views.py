from django.shortcuts import render
from .models import Buy
from .forms import RegistrationForm
import datetime 
def Home(request):
  buys = Buy.objects
  time = datetime.datetime.now()

  context ={
    'buys':buys,
    'time':time
  }

  return render(request,'home.html',context)

def register(request):
  context={
    'form':RegistrationForm
  }
  return render(request,'register.html',context)  