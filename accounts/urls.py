from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('/login', login, name='login'),
    path('/register', register, name='register'),
    path('/logout', logout, name='logout'),
]