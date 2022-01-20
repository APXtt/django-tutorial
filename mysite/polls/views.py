from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id): #질문 페이지
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id): #질문 결과 페이지
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id): #질문 세부 페이지 (투표페이지)
    return HttpResponse("You're voting on question %s." % question_id)