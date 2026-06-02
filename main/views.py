from django.shortcuts import render
from django.views.generic import ListView
from .models import Car, Color
# Create your views here.

class CarListView(ListView):
    model = Car
    template_name = 'main/car_list.html'
    context_object_name = 'cars'
