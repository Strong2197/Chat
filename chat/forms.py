from django import forms

from .models import Message


class ChatForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('text',)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
