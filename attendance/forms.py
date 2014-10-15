from django.contrib.auth.forms import UserCreationForm
from django import forms

__author__ = 'danielsiker'

class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Person
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "phone")
        # inherits from usercreation form to check passwords, validation, etc

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Person.objects.get(username=username)
        except Person.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )