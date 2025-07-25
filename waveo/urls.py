from django.conf.urls.static import static
from django.urls import path

from WebProject import settings
from . import views

app_name = 'waveo'
urlpatterns = [
    path("", views.home),
    path("create/<str:notes>", views.create),
    path("view/<str:name>", views.recall)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
