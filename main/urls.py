# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main page with Contact, Gallery, and Events
    path('events_list/', views.events_list, name='events_list'), 
]
