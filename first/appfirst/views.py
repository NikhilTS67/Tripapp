import requests
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from. models import album

# Create your views here.


def fstfn(requests):
    obj = album.objects.all()
    return render(requests, 'index.html', {'result': obj})



# def sndfn(requests):
#     return render(requests,'snd.html')
#
# def thdfn(requests):
#    return HttpResponse('Third Response')
#
# def forfn(requests):
#     return render(requests, 'frt.html')