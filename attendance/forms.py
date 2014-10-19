from django import forms
from django.contrib.auth.forms import UserCreationForm
from attendance.models import CheckIn, Profile


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "teacher")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Profile.objects.get(username=username)
        except Profile.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class CheckInForm(forms.ModelForm):

    class Meta:
        model = CheckIn