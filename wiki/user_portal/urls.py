# user_portal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_portal, name='user_portal'),
]
