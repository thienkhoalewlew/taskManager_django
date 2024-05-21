from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm, UpdateProfileForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from .models import Task,User,Profile

from django.contrib import messages

# Create your views here.
def home(request):

    return render(request, 'index.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)

            form.save()

            profile = Profile.objects.create(user=current_user)

            messages.success(request, "Account was created for " + form.cleaned_data['username'])

            return redirect('my_login')
    context = {'form': form}
    return render(request, 'register.html', context=context)

def my_login(request):
    form = LoginForm

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'login.html', context=context)

@login_required(login_url='my_login')
def dashboard(request):
    profile_pic = Profile.objects.get(user=request.user)
    context = {'profile': profile_pic}

    return render(request, 'profile/dashboard.html', context=context)

@login_required(login_url='my_login')
def createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user

            task.save()

            return redirect('view_tasks')
    context = {'form': form}
    return render(request, 'profile/create-task.html', context=context)
@login_required(login_url='my_login')
def viewTasks(request):
    current_user = request.user.id
    task = Task.objects.all().filter(user=current_user)
    context = {'task': task}

    return render(request, 'profile/view_tasks.html', context=context)

@login_required(login_url='my_login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_tasks')
    context = {'form': form}
    return render(request, 'profile/update_task.html', context=context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()

        return redirect('view_tasks')

    return render(request, 'profile/delete_task.html')

@login_required(login_url='my_login')
def profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile = Profile.objects.get(user=request.user)

    form2 = UpdateProfileForm(instance=profile)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        form2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid():
            user_form.save()

            return redirect('dashboard')

        if form2.is_valid():
            form2.save()

            return redirect('dashboard')

    context = {'user_form': user_form, 'form2': form2}
    return render(request, 'profile/profile-management.html', context=context)

@login_required(login_url='my_login')
def deleteAccount(request):
    if request.method == 'POST':
        delete_user = User.objects.get(username=request.user)
        delete_user.delete()

        return redirect('')

    return render(request, 'profile/delete-account.html')

def logout(request):
    auth.logout(request)
    return redirect('')