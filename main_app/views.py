from django.shortcuts import render
from .models import Coin
# Create your views here.

# Define the home view
def home(request):
  # Must include a .html file exstension. 
  return render(request, 'home.html')

def about(request):
  # render the about.html file when htttp request is processed. 
  return render(request, 'about.html')

def coins_index(request):
  coins = Coin.objects.all()
  # render the coins/index.html template when http request. 
  return render(request, 'coins/index.html' , { 'coins': coins})