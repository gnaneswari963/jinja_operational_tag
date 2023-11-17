from django.shortcuts import render

# Create your views here.

def operation(request):
    d={'a':90}
    return render(request,'operation.html',d)

def ifelse(request):
    d={'a':10,'b':20}
    return render(request,'ifelse.html',d)

def ifelif(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'ifelif.html',d)

def nestedif(request):
    d={'a':100,'b':20,'c':30}
    return render(request,'nestedif.html',d)



