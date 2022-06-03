from django.shortcuts import render
from django.http import HttpResponse


def all_shoes(request):
    return HttpResponse('To są wszystkie buty')


def about_us(request):
    return HttpResponse('O nas:')


def shoes_home(request):
    return HttpResponse('Strona główna:')


# Create your views here.
