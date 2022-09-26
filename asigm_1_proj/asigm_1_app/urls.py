from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('register', views.register, name='register'),
]