from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.postgres.forms import SimpleArrayField
from django.forms import ModelForm
from .models import Poll, Option
from django import forms


class PollForm(ModelForm):
    options = SimpleArrayField(forms.CharField(max_length=5))

    class Meta:
        model = Poll
        fields = ['question']


class OptionForm(ModelForm):
    class Meta:
        model = Option
        fields = ['option']
