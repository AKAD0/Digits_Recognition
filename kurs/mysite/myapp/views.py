from django.http import HttpResponse
from django.shortcuts import render #Allows to render html

def Page1(request):
    return render(request,'Page1.html')