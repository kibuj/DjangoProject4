from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('', views.feed, name='feed'),
    path('<slug:slug>/edit/', views.post_edit, name='post_edit'),
]