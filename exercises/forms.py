
from django import forms

class AnswerForm(forms.Form):
    user_answer = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={
            'placeholder': 'your answer...',
            'autofocus': 'autofocus',
        })
    )