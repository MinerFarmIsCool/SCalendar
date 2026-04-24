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
    security_level = models.IntegerField(default=5)
    opacity = models.IntegerField(default=100)

    def calculate_duration(self):
        if self.all_day:
            return 24
        return 1

    def validate_opacity(self): # Can't validate opacity in the database, so we do it here, if it's an invalid value, it will be set to 100. This will also be done in the form, so this code is mostly a double checker
        if self.opacity < 0 or self.opacity > 100:
            self.opacity = 100

    def __str__(self):
        return self.name

    def validate_time(self):
        meow1 = self.start_time.replace(tzinfo=None)
        meow2 = self.end_time.replace(tzinfo=None)
        if self.start_time > self.end_time:
            raise ValidationError("Start time must be before end time")
        if meow1 < datetime(2000, 1, 1, 0, 0):
            raise ValidationError("Start time must be after 1/1/2000")
        if meow2 > datetime(2050, 1, 1, 0, 0):
            raise ValidationError("End time must be before 1/1/2050")




