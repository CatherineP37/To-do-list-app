from django import forms
from django.forms import ModelForm
from .models import TaskList

class AddTask(ModelForm):
    class Meta:
        model = TaskList
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Enter your task here'}),
        }