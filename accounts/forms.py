from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'user_permissions')


class CustomUserChageForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'user_permissions')