# 🎵 Waveo — Django App

This is the Django backend for **Waveo**, an interactive music visualization platform.

🏆 **Created for [DemonHacks 2020](https://devpost.com/software/waveo)**  
🏅 Winner of the **"Hack the Arts"** category

📺 **[Video Demo](https://www.youtube.com/watch?v=mUGjUHDetPc)**

---

## 🚀 Running Locally

To get started with Waveo on your local machine:

1. Clone the repository
2. Run `pip install -r requirements.txt` to install the dependencies
3. Generate static files:
   ```bash
   python manage.py collectstatic
   ```
4. Run `python manage.py runserver` to start the server
5. Go to [http://localhost:8000](http://localhost:8000) in your browser

---

## 🧩 Integrating into Another Django Project

1. Clone the repository
2. Run `pip install -r requirements.txt` to install the dependencies
3. Add the `waveo` folder to your Django project directory (same level as your other apps)
4. Update your `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...,
       'waveo',
   ]
   ```
5. Update your `urls.py`:

   At the top:
   ```python
   from django.urls import include, path
   ```
   In `urlpatterns`:
   ```python
   path('', include('waveo.urls')),
   ```
6. Generate static files:
   ```bash
   python manage.py collectstatic
   ```
7. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
