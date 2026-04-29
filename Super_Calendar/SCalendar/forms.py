from datetime import datetime

from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    start_time = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )
    )
    end_time = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )
    )
    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Event
        fields = ['name', 'description', 'start_time', 'end_time', 'all_day', 'location', 'display_color', 'security_level', 'opacity', 'repeat']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter location'}),
            'display_color': forms.ColorInput(),
            'opacity': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }

    def save(self, commit=True):
        event = super().save(commit=False)
        event.profile = self.profile
        event.validate_opacity()
        event.validate_time()
        event.calculate_duration()
        if commit:
            event.save()
        return event