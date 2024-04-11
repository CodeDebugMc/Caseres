from django.urls import path
from . import views

urlpatterns = [
    path('MyHome', views.home, name='home'),
    #dosomething
]