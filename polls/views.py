from django.shortcuts import render
from polls.models import Question
from django.http import HttpResponse
# Create your views here.
path='polls/'
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)
    #return render(request,path+'index.html')
    #html="<html><h2>poll application</h2></html>"
    #return HttpResponse(html)
def detail(request,question_id):
    return render(request,path+'detail.html')
def results(request,question_id):
    
    return render(request,path+'results.html')
def vote(request,question_id):

    return render(request,path+'vote.html')
