from django.test import TestCase

# Create your tests here.
from django.core import mail
from django.core.exceptions import ValidationError
from django.test import TestCase
from attendance.forms import EmailUserCreationForm
from attendance.models import Person

#
# class FormTestCase(TestCase):
#     def test_clean_username_exception(self):
#         # Create a player so that this username we're testing is already taken
#         Person.objects.create_user(username='test-user')
#
#         # set up the form for testing
#         form = EmailUserCreationForm()
#         form.cleaned_data = {'username': 'test-user'}
#
#         # use a context manager to watch for the validation error being raised
#         with self.assertRaises(ValidationError):
#             form.clean_username()

    # def test_clean_username(self):
    #     # Create a player so that this username we're testing is already taken
    #     Person.objects.create_user(username='test-user2')
    #
    #     # set up the form for testing
    #     form = EmailUserCreationForm()
    #     form.cleaned_data = {'username': 'test-user'}
    #
    #     # use a context manager to watch for the validation error being raised
    #     form.clean_username()

    # def test_register_sends_email(self):
    #     form = EmailUserCreationForm()
    #     form.cleaned_data = {
    #         'username': 'test',
    #         'email': 'test@test.com',
    #         'password1': 'test-pw',
    #         'password2': 'test-pw',
    #     }
    #     form.save()
    #     # Check there is an email to send
    #     self.assertEqual(len(mail.outbox), 1)
    #     # Check the subject is what we expect
    #     self.assertEqual(mail.outbox[0].subject, 'Welcome!')


class ModelTestCase(TestCase):
    def setUp(self):
        self.teacher = Person.objects.create(teacher=True)
        self.not_teacher = Person.objects.create(teacher=False)

    def test_is_teacher(self):
        self.assertEqual(self.teacher(self.teacher), True)