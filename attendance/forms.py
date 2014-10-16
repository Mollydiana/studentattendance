from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django import forms
from attendance.models import Person, Course


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Person
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "teacher")
        # inherits from usercreation form to check passwords, validation, etc

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Person.objects.get(username="username")
        except Person.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class StudentCheckInForm(forms.Form):
    classes = forms.ChoiceField(widget=forms.RadioSelect, choices=[])
    helper = FormHelper()
    helper.form_method = "POST"
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('Checkin', 'Checkin', css_class='btn-default'))

    # Initialize and populate the classes selections
    # Pass in student objects
    def __init__(self, student, *args, **kwargs):
        super(StudentCheckInForm, self).__init__(*args, **kwargs)
        self.fields['courses'].choices = [
            (Course.pk, Course.name)
            for courses in Course.objects.filter(student=student)
        ]