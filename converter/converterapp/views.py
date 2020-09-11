from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def convert(request):

    try:
        q = int(request.GET['query'])
        isClassic = request.GET.get('classic')
        classis = " "
        if isClassic:
            dollar = q*5.63
            classic="Classic"
        else:
            dollar = q*365
            classic=""
        mdictionary = {
            "q" : q,
            "ans" : dollar,
            "cl":classic
        }
        return render(request,'index.html',context = mdictionary)

    except:
        mdictionary={
            "error":True
        }
        return render(request,'index.html',context = mdictionary)
