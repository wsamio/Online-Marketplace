from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from item.models import Item

def registerUser(request):

    if request.user.is_authenticated:
        return redirect('all-items')

    # creating the instance of the form
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            return redirect('login')

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

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('all-items')

@login_required(login_url='login')
def userDash(request):
    owner = request.user
    Sold = Item.objects.filter(is_sold=True, created_by=owner)
    Unsold = Item.objects.filter(is_sold=False, created_by=owner)

    context = {'Sold' : Sold, 'Unsold' : Unsold}

    return render(request, 'users/dashboard.html', context)
