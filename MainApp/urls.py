from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkView, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),  
]