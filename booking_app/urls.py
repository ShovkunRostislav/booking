from django.urls import path
from auth_sys import views
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('places', views.place_list, name='places'),
    path('book', views.book_flight, name='book_flight'),
]