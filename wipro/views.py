import datetime

from django.shortcuts import render


def home(request):
    datenow = datetime.datetime.today().date()
    timenow = datetime.datetime.today().time()
    print(datenow)
    print(timenow)
    context = {
        'date': datenow,
        'time': timenow
    }
    return render(request,'homepage.html',context)




