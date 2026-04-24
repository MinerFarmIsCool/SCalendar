from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_event/', views.create_event, name='create_event'),
    path('event_list/', views.event_list, name='event_list'),
]