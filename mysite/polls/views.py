from django.http import HttpRequest
from django.http.response import HttpResponse

def index(request):
    return HttpResponse("hello world, you're at the polls index.")