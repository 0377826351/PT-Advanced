from django.urls import path
from .views import show_info,show_info_detail

urlpatterns = [
    path('list_ct',show_info),
    path('list_ct/<str:detail>',show_info_detail),
]