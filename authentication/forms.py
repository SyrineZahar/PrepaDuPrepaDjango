from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=(
        ('ROLE_STUDENT', 'Student'),
        ('ROLE_TEACHER', 'Teacher'),
        ('ROLE_ADMIN', 'Admin')
    ))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        custom_user = CustomUser(user=user)
        custom_user.email = self.cleaned_data['email']
        custom_user.role = self.cleaned_data['role']
        if commit:
            custom_user.save()
        return user
