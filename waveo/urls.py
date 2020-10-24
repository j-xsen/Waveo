from django.urls import path

from . import views

app_name = 'waveo'
urlpatterns = [
    path("",views.home)
]