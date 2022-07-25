import re
from django.http import HttpResponse
from django.shortcuts import render


def news(request):

    return render(request, 'home2.html')

def twone(request):
    return render(request, 'home.html')