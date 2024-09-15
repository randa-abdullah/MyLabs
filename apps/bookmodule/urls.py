# apps/bookmodule/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('index2/<int:val1>/<int:val2>/', views.index2, name='index2'),
]
