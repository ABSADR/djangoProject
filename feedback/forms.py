from django import forms
from django.forms import TextInput, EmailInput, Textarea, DateInput, Select

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'email', 'trainer', 'message', 'active',
                  ]

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name here'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name here'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email here'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
            'created_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'updated_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': Select(attrs={'class': 'form-select'})

        }


class FeedbackUpdateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'email', 'trainer', 'message', 'active',
                  ]

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name here'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name here'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email here'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
            'created_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'updated_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': Select(attrs={'class': 'form-select'})

        }