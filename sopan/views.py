from django.shortcuts import render

# Create your views here.
from sopan.models import Python, Java, Save, Intel


def home(request):
    return render(request, 'index.html')


def python(request):
    data = Python.objects.all()
    return render(request, 'python.html', {'data': data})


def java(request):
    return render(request, 'java.html')



def save(request):
    image = Save.objects.all()
    data = {
            'image': image,

        }
    return render(request, 'save.html', data)



def intel(request):
    data = Intel.objects.all()
    return render(request, 'intel.html',{'data': data})
