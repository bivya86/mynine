from django.shortcuts import render

# Create your views here.

def print1(request):
    d={'name':'DIVYA'}
    return render(request,'print1.html',context=d)