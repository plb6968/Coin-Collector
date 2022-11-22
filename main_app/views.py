from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Coin, Case
from .forms import MaterialForm
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

def coin_details(request, coin_id):
  # Assign the requested coin to the variable coin. 
  coin = Coin.objects.get(id=coin_id)
  # instantiate MaterialForm to be rendered in template
  material_form = MaterialForm
  return render(request, 'coins/details.html', { 
    'coin': coin, 'material_form': material_form
    })

class CoinCreate(CreateView):
  model = Coin
  fields = ['name', 'rarity', 'value']

class CoinUpdate(UpdateView):
  model = Coin
  fields = ['rarity', 'value']

class CoinDelete(DeleteView):
  model = Coin
  success_url = '/coins'

def add_material(request, coin_id):
  # create a ModelForm instance using
  #  the data that was submitted in the form.
  form = MaterialForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # We cant save to the db yet
    # because we have not assigned the 
    # cat_id FK.
    new_material = form.save(commit=False)
    new_material.coin_id = coin_id
    new_material.save()
  return redirect('coin_details', coin_id=coin_id)

class CaseCreate(CreateView):
  model = Case
  fields = '__all__'

class CaseDetail(DetailView):
  model = Case

class CaseList(ListView):
  model = Case

class CaseUpdate(UpdateView):
  model = Case
  fields = '__all__'

class CaseDelete(DeleteView):
  model = Case
  success_url = '/case'