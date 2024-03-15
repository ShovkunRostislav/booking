from django.urls import path
from .views import *

urlpatterns = [
    path('regist', register, name='register'),
    path('logout', logout_view, name='logout'),
    path('login', login_view, name='login')
]