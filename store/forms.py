from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='eg. youremail@gmail.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=50, required=True)
	name = forms.CharField(max_length=20, required=True)
	from_email = forms.EmailField(max_length=50, required=True)
	message = forms.CharField(
		max_length=500,
		widget=forms.Textarea(),
		help_text='write here your message!'
	)

