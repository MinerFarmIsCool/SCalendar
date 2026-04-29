from django.contrib import admin
from .models import *

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'location', 'description', 'security_level', 'duration', 'all_day', 'repeat', 'display_color', 'created_at', 'last_updated_at', 'opacity')
    list_filter = ('start_time', 'end_time')
    search_fields = ('name', 'start_time', 'end_time')