from django.urls import path
from myapp import views
from . import views

urlpatterns =[
    path("", views.home, name="home"),

]