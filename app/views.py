from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':1909,'b':2090,'c':20099}
    return render(request,'conditions.html',context=d)


def loop(request):
    d={'name':'ASHU'}
    return render(request,'loop.html',d)