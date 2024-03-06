from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class UserProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']