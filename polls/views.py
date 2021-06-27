from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
path='polls/'
def index(request):
    return render(request,path+'index.html')
    #html="<html><h2>poll application</h2></html>"
    #return HttpResponse(html)
def detail(request,question_id):
    return render(request,path+'detail.html')
def results(request,question_id):
    
    return render(request,path+'results.html')
def vote(request,question_id):

    return render(request,path+'vote.html')
