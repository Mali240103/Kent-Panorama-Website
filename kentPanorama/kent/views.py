from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Villa
 
# Create your views here.

def homepage(request):
    return render(request,"homepage.html")

def kupikInsaat(request):
    return render(request,"kupikInsaat.html")



def konsept(request):
    return render(request,"konsept.html")

def konum(request):
    return render(request,"konum.html")

def projePlani(request):
    return render(request,"projePlani.html")




