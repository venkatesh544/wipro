from django.urls import path

from venkat1 import views

urlpatterns = [
    path('bdaloginpage', views.bdaloginpage, name='bdaloginpage')

]