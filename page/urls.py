from django.contrib import admin
from django.urls import path, include
from page import views

app_name = 'page'

urlpatterns = [
    path('', views.index, name='index'),
    path('partner/', views.partner, name='partner'),
    path('detail/', views.detail, name='detail'),
    path('write/', views.write , name="write"),
]
