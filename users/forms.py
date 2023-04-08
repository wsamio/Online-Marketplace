from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder' : '@samio',
#         'class' : 'text-sm w-full py-2 px-6 rounded-lg'
#     }))

#     password = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder' : '•••••••••••',
#         'class' : 'text-sm w-full py-2 px-6 rounded-lg'
#     }))



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name' : 'Name',
        }
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Misbah Samio',
        'class' : 'text-sm w-full py-2 px-6 rounded-lg'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : '@samio',
        'class' : 'text-sm w-full py-2 px-6 rounded-lg'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'samio@email.com',
        'class' : 'text-sm w-full py-2 px-6 rounded-lg'
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : '•••••••••••',
        'class' : 'text-sm w-full py-2 px-6 rounded-lg'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : '•••••••••••',
        'class' : 'text-sm w-full py-2 px-6 rounded-lg'
    }))





    