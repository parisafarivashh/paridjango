from django.urls import path
from .views import Home,register

urlpatterns = [
    path('home/',Home,name='home'),
    path('',register,name='register')
]
