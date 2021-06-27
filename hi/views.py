from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    #curTime=datetime.datetime.now()
    #html=f"<html><h1>{curTime}</h1></html>"
    #return HttpResponse(html)
    return render(request,'hi/home.html')
