# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('/login', views.login_view, name='login'),
    path('/generate_token', views.generate_token_view, name='generate_token'),
    path('/register', views.register, name='register'),
]