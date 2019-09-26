from django import forms
from django.forms import ModelForm
from .models import Event, Category

class DateInput(forms.DateInput):
   input_type = 'date'

class TimeInput(forms.TimeInput):
   input_type = 'time'


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 
            'venue', 
            'location',
            'start_time',
            'end_time',
            'start_date',
            'end_date',
            'categories',
            ]
        widgets = {
           'start_time': TimeInput(), 
           'end_time': TimeInput(),
           'start_date': DateInput(), 
           'end_date': DateInput(),
       }
