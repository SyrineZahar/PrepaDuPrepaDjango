from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import CustomUser

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField()
    class Meta:
        model=User 
        fields=('username'
            'password1',
            'password2'
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        custom_user = CustomUser(user=user, role=user)

        if commit:
            custom_user.save()
        return user  