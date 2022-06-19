from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Shoes
from .forms import ShoesForm



def all_shoes(request):
    shoes_list = Shoes.objects.all()
    #return HttpResponse('To są wszystkie buty')
    return render(request, 'shoes.html',{'shoes_list': shoes_list})


def about_us(request):
    return HttpResponse('O nas:')


def shoes_home(request):
    return HttpResponse('Strona główna:')


def create_shoes(request):
    form = ShoesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'create_edit_shoes.html', {'form': form})


def edit_shoes(request, id):
    shoes = Shoes.objects.get(pk = id)
    form = ShoesForm(request.POST or None, request.FILES or None, instance=shoes)
    if form.is_valid():
        form.save()
        return redirect(all_shoes)
    return render(request, 'create_edit_shoes.html', {'form': form})


# Create your views here.
