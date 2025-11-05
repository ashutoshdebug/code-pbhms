from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'guests'
urlpatterns = [
    path('', views.guests, name = 'home'),
    path('checkin/', views.checkin, name = 'checkin'),
    path('checkout/', views.checkout, name = 'checkout'),
]