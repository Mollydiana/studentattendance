import datetime
<<<<<<< Updated upstream
import json
from django.conf import settings
from django.core import serializers
from django.db.models import Max
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from attendance.forms import EmailUserCreationForm, StudentCheckInForm
from attendance.models import Person, Course, CheckIn
=======

from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Max
from django.shortcuts import render, redirect



# Create your views here.
from studentattendance.forms import EmailUserCreationForm
from studentattendance import settings
>>>>>>> Stashed changes


def home(request):
    return render(request, 'home.html')

<<<<<<< Updated upstream
def profile(request):
    return render(request, 'profile.html')


=======
>>>>>>> Stashed changes
@login_required
def student(request):
    if not request.user.is_authenticated():
        return redirect('home')
    now = datetime.datetime.now()
<<<<<<< Updated upstream
    mayor = Person.objects.all().aggregate(Max('check_ins'))
    return render(request, 'profile.html', {
        'now': now,
        'mayor': mayor
=======
    attendance = Person.checkins
    mayor = attendance.aggregate(Max('checkins'))
    return render(request, 'student.html', {
        'now': now
>>>>>>> Stashed changes
    })

@login_required
def teacher(request):
    if not request.user.is_authenticated():
        return redirect('home')
    now = datetime.datetime.now()
<<<<<<< Updated upstream
    mayor = Person.objects.all().aggregate(Max('check_ins'))
    return render(request, 'profile.html', {
        'now': now,
        'mayor': mayor
=======
    mayor = Person.checkins.aggregate(Max('checkins'))
    return render(request, 'teacher.html', {
        'now': now
>>>>>>> Stashed changes
    })


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            # user.email_user("Welcome!", "Thank you for signing up for our website.")
<<<<<<< Updated upstream
            # text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            # html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site. ' \
            #                'You registered at {}.</div>'.format(user.first_name, user.last_name, user.date_joined)
            # msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect("profile")
=======
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
>>>>>>> Stashed changes
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
<<<<<<< Updated upstream

@login_required()
def checkin(request):
    student_check_in_form = None
    if request.user.is_student:
    #Check if student or teacher
        student_check_in_form = StudentCheckInForm(student=request.user)
        #Pass in student user to get classes for the particular student in form
        if request.method == "POST":
            student_check_in_form = StudentCheckInForm(request.POST)
            if student_check_in_form.is_valid():
                checkin = CheckIn.objects.create(
                    student=request.user,
                    class_name=Course.objects.get(
                        pk=int(student_check_in_form.cleaned_data['classes'])
                    )
                )
                if checkin:
                    return redirect('home')

    data = {'student_check_in_form': student_check_in_form}
    return render(request, 'profile.html', data)


@csrf_exempt
def ajax_checkin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data and request.user.is_student:
            checkin = CheckIn.objects.create(
                    student=request.user,
                    class_name=Course.objects.get(
                        pk=int(data['class_id'])
                    )
                )
            if checkin:
                response = serializers.serialize('json', [checkin])
                return HttpResponse(response, content_type='application/json')

=======
>>>>>>> Stashed changes
