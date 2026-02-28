from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import never_cache
from .forms import RegisterForm, TaskForm
from .models import Task


def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'register.html', {'form': form})


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html', {'form': form})

@never_cache
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@never_cache
def dashboard(request):
    pending_tasks = Task.objects.filter(user=request.user, completed=False)
    completed_tasks = Task.objects.filter(user=request.user, completed=True)

    context = {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'dashboard.html', context)

@login_required
def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('dashboard')

@login_required
@never_cache
def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')

    return render(request, 'create.html', {'form': form})

@login_required
@never_cache
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'update.html', {'form': form})

@login_required
@never_cache
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')

    return render(request, 'delete.html', {'task': task})

@login_required
@never_cache
def view_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'view.html', {'task': task})

@login_required
@never_cache
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')

    return render(request, 'profile.html', {'user': user})

