from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
path=''
def index(request):
    return render(request,path+'index.html')
    #html="<html><h2>poll application</h2></html>"
    #return HttpResponse(html)
def detail(request):
    return render(request,path+'detail.html')
def results(request):
    
    return render(request,path+'results.html')
def vote(request):

    return render(request,path+'vote.html')
