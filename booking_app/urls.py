from django.urls import path
from auth_sys import views
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('places', views.place_list, name='places'),
    path('book', views.create_booking, name='book_flight'),
    path('album', views.Album, name='album'),
    path('pln1', views.alb1, name='link1'),
    path('pln2', views.alb2, name='link2'),
    path('pln3', views.alb3, name='link3'),
]