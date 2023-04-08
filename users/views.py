from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

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


