from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from attendance.forms import EmailUserCreationForm
from attendance.models import CheckIn, Profile


def dropdown(request):
    return render(request, 'dropdown.html')

def home(request):
    mayor = Profile.objects.order_by('-count')[0]
    user = request.user
    user_check_ins = CheckIn.objects.filter(student__id=user.id)
    in_today = 0
    if request.method == 'POST':
        user = request.user
        check_in = CheckIn.objects.create(student=user)
        check_in.save()
        user.count += 1
        user.save()
        return redirect('profile')
    else:
        for checkin in user_check_ins:
            if checkin.time.day == datetime.today().day:
                in_today = 1
                data = {'message': 'THANKS FOR CHECKIN THE FUCK IN', 'mayor': mayor, 'in_today': in_today}
                return render(request, 'home.html', data)
    data = {'message': 'CHECK THE FUCK IN', 'mayor': mayor, 'in_today': in_today}
    return render(request, 'home.html', data)


def register(request):
    if request.method == "POST":
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = EmailUserCreationForm()
    return render(request, "registration/register.html", {'form': form})


@login_required
def profile(request):
    user = request.user
    mayor = Profile.objects.order_by('-count')[0]
    if user.teacher:
        data = {
            'attendance': CheckIn.objects.filter(time__lte=datetime.today()),
            'mayor': mayor
        }
        return render(request, 'teacher.html', data)

    else:
        checkin_list = CheckIn.objects.filter(student=request.user)
        data = {'checkin_list': checkin_list}
        # return render(request, 'profile.html', data)
        mayor = Profile.objects.order_by('-count')[0]
        user = request.user
        user_check_ins = CheckIn.objects.filter(student__id=user.id)
        in_today = 0
        if request.method == 'POST':
            user = request.user
            check_in = CheckIn.objects.create(student=user)
            check_in.save()
            user.count += 1
            user.save()
            return redirect('profile')
        else:
            for checkin in user_check_ins:
                if checkin.time.day == datetime.today().day:
                    in_today = 1
                    data = {'message': 'Get back to work!', 'mayor': mayor, 'in_today': in_today}
                    return render(request, 'home.html', data)
        data = {'message': 'Please check in', 'mayor': mayor, 'in_today': in_today}
        return render(request, 'home.html', data)

