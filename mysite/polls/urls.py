from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'), # /polls
    path('<int:question_id>/', views.detail, name='detail'), #질문 페이지 /polls/<question_id>/
    path('<int:question_id>/results/', views.results, name='results'), #질문 결과 페이지 /polls/<question_id>/results
    path('<int:question_id>/vote/', views.vote, name='vote'), #질문 세부 페이지 /polls/<question_id>/vote
]