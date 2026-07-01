from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from django.contrib.auth.decorators import login_required

from .models import Event


# Create your views here.
@login_required(login_url="users:login")
def home(request):
    return render(request, "SCalendar/home.html")

@login_required(login_url="users:login")
def create_event(request): # Makes event using the event form
    if request.method == "POST":
        form = EventForm(request.POST, profile=request.user.profile)
        if form.is_valid():
            event = form.save()
            messages.success(request, f"Event '{event.name}' created successfully.")
            return redirect("SCalendar:home")
    else:
        form = EventForm(profile = request.user.profile)
    return render(request, "SCalendar/create_event.html", {"form": form})

@login_required(login_url="users:login")
def event_list(request):
    events = Event.objects.all()
    return render(request, "SCalendar/event_list.html", {"events": events})

def edit_event(request, event_id): # Gets event then sends the data in the event to the make event page to then be remade
    event = get_object_or_404(Event, pk=event_id)
    if request.user.profile != event.profile:
        return redirect("SCalendar:home")
    if request.method == "POST":
        form = EventForm(request.POST, profile=request.user.profile, instance=event)
        if form.is_valid():
            event = form.save()
            messages.success(request, f"Event '{event.name}' updated successfully.")
            return redirect("SCalendar:home")
    else:
        form = EventForm(profile=request.user.profile, instance=event)
    return render(request, "SCalendar/create_event.html", {"form": form})

@login_required(login_url="users:login")
def delete_event(request, event_id): # Deletes the event after checking if the user is the user who made the event
    event = get_object_or_404(Event, pk=event_id)
    if request.user.profile == event.profile:
        event.delete()
        messages.success(request, f"Event '{event.name}' deleted successfully.")
    else:
        messages.error(request, f"Event '{event.name}' not deleted. You are not allowed to delete this event.")
    return redirect("SCalendar:home")

@login_required(login_url="users:login")
def view_personal_calendar(request):
    raw_events = Event.objects.filter(profile = request.user.profile)
    events = []
    for event in raw_events:
        event_dict = event_to_dict(event)
        events.append(event_dict)
        print(events)

    return render(request, "SCalendar/personal_calendar.html", {"events": events})
# converts the event object to a dictionary for rendering with javascript
def event_to_dict(event):
    if event.all_day:
        new_dict = {
            "title": event.name,
            "start": event.start_time.isoformat(),
            "description": event.description,
            "location": event.location,
            "backgroundColor": event.display_color,
            "allDay": event.all_day,
            "pk": event.pk
        }
    else:
        new_dict = {
            "title": event.name,
            "start": event.start_time.isoformat(),
            "end": event.end_time.isoformat(),
            "description": event.description,
            "location": event.location,
            "backgroundColor": event.display_color,
            "pk": event.pk
        }
    return new_dict
