from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random

# Create your views here.
def home(request):
    rand_num = random.randrange(1, 12974)

    context = {
        'rand_num' : rand_num
    }
    return render(request, 'home.html', context=context)