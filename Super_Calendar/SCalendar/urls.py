from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_event/', views.create_event, name='create_event'),
    path('event/<int:event_id>/delete', views.delete_event, name='delete_event'),
    path('event/<int:event_id>/edit', views.edit_event, name='edit_event'),
    path('event_list/', views.event_list, name='event_list'),
]