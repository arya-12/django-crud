# app/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg bg-white/20 backdrop-blur text-white focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter title...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 rounded-lg bg-white/20 backdrop-blur text-white focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter description...',
                'rows': 4
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-blue-500'
            })
        }
