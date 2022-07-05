from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Shoes, MoreInfo
from .forms import ShoesForm, MoreInfoForm
from django.contrib.auth.decorators import login_required


def homepage(request):

    return render(request, 'homepage.html')


def all_shoes(request):

    shoes_list = Shoes.objects.all()
    return render(request, 'shoes.html',{'shoes_list': shoes_list})

@login_required
def create_shoes(request):

    form_shoes = ShoesForm(request.POST or None, request.FILES or None)
    form_info = MoreInfoForm(request.POST or None)
    if all((form_shoes.is_valid(), form_info.is_valid())):
        shoes = form_shoes.save(commit=False)
        shoes.more_info = form_info.save()
        shoes.save()
        return redirect(all_shoes)
    return render(request, 'create_edit_shoes.html', {'form': form_shoes, 'form_info': form_info, 'if_new': True})

@login_required
def edit_shoes(request, id):

    shoes = get_object_or_404(Shoes, pk=id)

    try:
        more_info = MoreInfo.objects.get(shoes=shoes.id)
    except MoreInfo.DoesNotExist:
        more_info = None

    form_shoes = ShoesForm(request.POST or None, request.FILES or None, instance=shoes)
    form_info = MoreInfoForm(request.POST or None, instance=more_info)
    if all((form_shoes.is_valid(), form_info.is_valid())):
        shoes = form_shoes.save(commit=False)
        shoes.more_info = form_info.save()
        shoes.save()
        return redirect(all_shoes)
    return render(request, 'create_edit_shoes.html', {'form': form_shoes, 'form_info': form_info, 'if_new': False})

@login_required
def delete_shoes(request, id):

    shoes = get_object_or_404(Shoes, pk=id)
    if request.method == "POST":
        shoes.delete()
        return redirect(all_shoes)
    return render(request, 'confirm.html', {'shoes': shoes})



# Create your views here.
