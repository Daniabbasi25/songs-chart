from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    songs=Songs.objects.all()
    return render(request,'index.html',{'songs':songs})