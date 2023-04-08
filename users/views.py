from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate

def registerUser(request):
    # creating the instance of the form
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()

        return redirect('all-items')

    context = {'form' : form}
    return render(request, 'users/register.html', context)


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('all-items')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('all-items')
        else:
            return redirect('blabla')

    return render(request, 'users/login.html')


