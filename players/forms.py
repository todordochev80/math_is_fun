from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age']

        labels = {
            'name': 'Child Name',
            'age': 'Age',
        }

        help_texts = {
            'age': 'Please enter an age between 4 and 12 years.',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter child name...',
                'class': 'form-control'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter age...',
                'class': 'form-control'
            }),
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age is not None:
            if age < 4:
                raise forms.ValidationError("The child is too young for these exercises. Minimum age is 4.")
            if age > 12:
                raise forms.ValidationError("These exercises might be too easy for you. Maximum age is 12.")

        return age