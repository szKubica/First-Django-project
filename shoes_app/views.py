from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Shoes
from .forms import ShoesForm
from django.contrib.auth.decorators import login_required


def homepage(request):

    return render(request, 'homepage.html')


def all_shoes(request):

    shoes_list = Shoes.objects.all()
    return render(request, 'shoes.html',{'shoes_list': shoes_list})

@login_required
def create_shoes(request):

    form = ShoesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(all_shoes)
    return render(request, 'create_edit_shoes.html', {'form': form})

@login_required
def edit_shoes(request, id):

    shoes = get_object_or_404(Shoes, pk=id)
    form = ShoesForm(request.POST or None, request.FILES or None, instance=shoes)
    if form.is_valid():
        form.save()
        return redirect(all_shoes)
    return render(request, 'create_edit_shoes.html', {'form': form})

@login_required
def delete_shoes(request, id):

    shoes = get_object_or_404(Shoes, pk=id)
    if request.method == "POST":
        shoes.delete()
        return redirect(all_shoes)
    return render(request, 'confirm.html', {'shoes': shoes})



# Create your views here.
