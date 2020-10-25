from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.
def home(request):
    args = {'notes': ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 'length': range(1, 13)}
    return TemplateResponse(request, "waveo/home.html", args)
