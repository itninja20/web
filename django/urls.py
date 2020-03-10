from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('server_list', views.server_list, name='server_list'),
]
