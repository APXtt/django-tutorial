from django.http import Http404, HttpRequest
from django.http.response import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

def detail(request, question_id): #질문 페이지
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'detail.html', context)

def results(request, question_id): #질문 결과 페이지
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id): #질문 세부 페이지 (투표페이지)
    return HttpResponse("You're voting on question %s." % question_id)