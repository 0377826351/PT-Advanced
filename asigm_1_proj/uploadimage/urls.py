from django.urls import path
from . import views

urlpatterns = [
    path('uploadimage', views.index, name='index'),
    path('animalform', views.animal, name='animal'),
]