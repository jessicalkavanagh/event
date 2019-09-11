from django.forms import ModelForm
from .models import Event, Category

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 
            'venue', 
            'location',
            'start_date',
            'start_time',
            'end_time',
            'categories',
            ]