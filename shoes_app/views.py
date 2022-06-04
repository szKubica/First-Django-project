from django.shortcuts import render
from django.http import HttpResponse
from .models import Shoes


def all_shoes(request):
    shoes_list = Shoes.objects.all()
    #return HttpResponse('To są wszystkie buty')
    return render(request, 'shoes.html',{'shoes_list': shoes_list})


def about_us(request):
    return HttpResponse('O nas:')


def shoes_home(request):
    return HttpResponse('Strona główna:')


# Create your views here.
