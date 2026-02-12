from django.forms import ModelForm
from .models import TaskList

class AddTask(ModelForm):
    class Meta:
        model = TaskList
        fields = ['title']