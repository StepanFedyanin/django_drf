from account.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
