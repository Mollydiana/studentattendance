import datetime
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Max
from django.shortcuts import render, redirect



# Create your views here.
from attendance.forms import EmailUserCreationForm


def home(request):
    return render(request, 'home.html')

@login_required
def student(request):
    if not request.user.is_authenticated():
        return redirect('home')
    now = datetime.datetime.now()
    attendance = Person.checkins
    mayor = attendance.aggregate(Max('checkins'))
    return render(request, 'student.html', {
        'now': now
    })

@login_required
def teacher(request):
    if not request.user.is_authenticated():
        return redirect('home')
    now = datetime.datetime.now()
    mayor = Person.checkins.aggregate(Max('checkins'))
    return render(request, 'teacher.html', {
        'now': now
    })


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            # user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site. ' \
                           'You registered at {}.</div>'.format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            if Person.teacher == True:
                return redirect("student")
            else:
                return redirect("teacher")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
