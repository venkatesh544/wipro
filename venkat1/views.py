from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from venkat1.models import venkat1


def bdaloginpage(request):

    if request.method == 'POST':
        context_id = ''
        context_password = ''

        userid = request.POST['userid']
        password = request.POST['userpassword']
        data = venkat1.objects.filter(userid=userid)
        if len(data) == 0:
           context_id = 'user not found'
           context_password = ''
        else:
            if password ==(data[0].password):

                context = {
                    'user1': data[0].userid,
                    'date': str(data[0].dateofjoining)[:10]
                }
                return render(request, 'navbars.html',context)
            else:
                context_id = ''
                context_password = 'your user id and password not matching '

        context = {
            'id': context_id,
            'password': context_password
        }

        return render(request, 'bdaloginpage.html', context)
    else:
        context = {
            'id': '',
            'password':''

        }
    return  render(request,'bdaloginpage.html',context)