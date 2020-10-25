from django.urls import path

from . import views

app_name = 'waveo'
urlpatterns = [
    path("", views.home),
    path("create/<str:notes>", views.create),
    path("view/<str:name>", views.recall)
]