from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question,Choice
# Create your views here.
def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'last_question_list' : last_question_list,
    }
    return render(request,'polls/index.html',context)

def details(request,question_id):
    response = "You're looking at question %s."
    return HttpResponse(response % question_id)

def results(request,question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)
    
def votes(request,question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)
