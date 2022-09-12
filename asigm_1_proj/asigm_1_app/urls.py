from django.urls import path

from . import views

urlpatterns = [
    path('asigm_1_app/', views.index, name='index'),
]