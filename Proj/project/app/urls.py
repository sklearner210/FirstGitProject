from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('index', views.index, name='app'),
    path('about', views.about, name='app'),
    path('contact', views.Contact, name='app'),
    path('services', views.Services, name='app')   
]