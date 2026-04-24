from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url="users:login")
def home(request):
    return render(request, "SCalendar/home.html")

@login_required(login_url="users:login")
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, profile=request.user.profile)
        if form.is_valid():
            event = form.save()
            messages.success(request, f"Event '{event.name}' created successfully.")
            return redirect("SCalendar:home")
    else:
        form = EventForm(profile = request.user.profile)
    return render(request, "SCalendar/create_event.html", {"form": form})