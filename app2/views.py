from django.shortcuts import render

# Create your views here.
def print2(request):
    d={'name':'DIA'}
    return render(request,'print2.html',context=d)