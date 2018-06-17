from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    # ex: /quiz/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /quiz/5/results/
    path('<int:question_id>/results/', views.results, name='results')
]
