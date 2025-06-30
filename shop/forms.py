from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = user.profile
            profile.phone_number = self.cleaned_data.get('phone_number')
            profile.address = self.cleaned_data.get('address')
            profile.save()
        return user 