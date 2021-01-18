This is the Django app of Waveo.

How to run locally:
1. Create a Django project
2. Install requirements.txt
3. Add the waveo folder to your project directory
4. Go into [project name]/settings.py and add "waveo" to `INSTALLED_APPS`
5. In [project name]/urls.py, add `from django.urls import include` at the top and
6. Also in [project name]/urls.py, add `path('', include('waveo.urls'))` to `urlpatterns`
7. Run the Django server
