from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse('To jest nasz pierwszy test')
    return render(request, "shoes.html")

# Create your views here.
