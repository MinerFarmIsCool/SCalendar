from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from users.models import Profile
from django.forms import fields
from datetime import datetime

# Create your models here.
class Event(models.Model):
    REPEAT_CHOICES = [
        ("never", "Never"),
        ("daily", "Daily"),
        ("weekly", "Weekly"),
        ("fortnightly", "Fortnightly"),
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = int
    all_day = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    repeat = models.CharField(max_length=20, choices=REPEAT_CHOICES, default="never")
    display_color = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    security_level = models.IntegerField(default=5) # NEED TO UPDATE TO REMOVE
    opacity = models.IntegerField(default=100)

    def calculate_duration(self):
        if self.all_day:
            self.duration = 24
        dur = self.start_time - self.end_time
        self.duration = dur.total_seconds() / 3600
        self.duration = round(self.duration, 2)

    def validate_opacity(self): # Can't validate opacity in the database, so we do it here, if it's an invalid value, it will be set to 100. This will also be done in the form, so this code is mostly a double checker
        if self.opacity < 0 or self.opacity > 100:
            self.opacity = 100

    def __str__(self):
        return self.name

    def validate_time(self):
        start_time = self.start_time.replace(tzinfo=None)
        end_time = self.end_time.replace(tzinfo=None)
        start_date = self.start_time.date()
        end_date = self.end_time.date()
        if self.start_time > self.end_time:
            raise ValidationError("Start time must be before end time")
        if start_time < datetime(2000, 1, 1, 0, 0):
            raise ValidationError("Start time must be after 1/1/2000")
        if end_time > datetime(2050, 1, 1, 0, 0):
            raise ValidationError("End time must be before 1/1/2050")
        if self.all_day:
            if start_date != end_date:
                raise ValidationError("Start day must be equal to end day")


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(Profile, related_name="members")
    admin_user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="admin_user")
    events = models.ManyToManyField(Event, related_name="events")

    





