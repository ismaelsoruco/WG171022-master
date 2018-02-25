from django import forms
from .models import CalendarEvent



class NewTask(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = [
            'title',
            'start',
            'end',
            'all_day',
            'url',
            'color',
            'responsable',
            'project',
            'comment',
            'status',
        ]