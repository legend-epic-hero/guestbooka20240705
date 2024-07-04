from django.shortcuts import render
from django.views.generic import ListView
from .models import Massage

# Create your views here.
class MassageList(ListView):
    model = Massage

    