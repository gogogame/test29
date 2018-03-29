from django.contrib import admin
from django.urls import include, path
from quiz import views

#
urlpatterns = [
    path('', views.home_page, name='home'),
]
