from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def polls_func(request):
    html="<html><h2>poll application</h2></html>"
    return HttpResponse(html)
