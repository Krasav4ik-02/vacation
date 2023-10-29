import pytz
from django.utils import timezone
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import *
from .models import *

def home(request):
    return render(request, 'home/home.html')

# def leave_request_list(request):
#     leave_requests = LeaveRequest.objects.filter(employee=request.user.employee)
#     return render(request, 'home/leave_request_list.html', {'leave_requests': leave_requests})

# def leave_request_create(request):
#     if request.method == 'POST':
#         form = LeaveRequestForm(request.POST)
#         if form.is_valid():
#             leave_request = form.save(commit=False)
#             leave_request.employee = request.user.employee
#             leave_request.save()
#             return redirect('leave_request_list')
#     else:
#         form = LeaveRequestForm()
#     return render(request, 'home/leave_request_form.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически входить в систему после регистрации
            return redirect('/')  # Замените 'home' на URL вашей домашней страницы
        else:
            return render(request, 'home/registration.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/registration.html', {'form': form})

def authentication(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'home/authentication.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def cabinet(request):
    user = request.user  # Получить текущего пользователя
    work_schedules = WorkSchedule.objects.filter(user=user)
    current_time = timezone.now().astimezone(pytz.timezone('Asia/Almaty')).time()
    work_status = "вне работы"

    try:
        position = Position.objects.get(user=user)
    except Position.DoesNotExist:
        position = None

    for schedule in work_schedules:
        if schedule.start_time <= current_time <= schedule.end_time:
            work_status = "на работе"
            break
    return render(request, 'home/cabinet.html', {'user': user, 'work_status': work_status, 'position': position, 'work_schedules': work_schedules})

@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('cabinet')

    else:
        form = UserEditForm(instance=user)

    return render(request, 'home/edit_profile.html', {'form': form})

def manager(request):
    users = User.objects.all()  # Получить всех пользователей
    return render(request, 'home/manager.html', {'users': users})