from django.urls import path
from .views import index, details, search

urlpatterns = [
    path('', index, name='listings'),
    path('<int:listings_id>', details, name='details'),
    path('search', search, name = 'search')
]