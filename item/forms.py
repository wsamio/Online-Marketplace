from django import forms
from django.forms import ModelForm
from . models import Item

class CreateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['created_by']

        widgets = {
            'category' : forms.Select(attrs={
                'class' : 'w-full py-2 px-6 rounded-lg border'
            }),
            'name': forms.TextInput(attrs={
                'class' : 'w-full py-2 px-6 rounded-lg border'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'w-full py-2 px-6 rounded-lg border'
            }),
            'featured_image' : forms.FileInput(attrs={
                'class' : 'w-full py-2 px-6 rounded-lg border'
            }),
            'price' : forms.TextInput(attrs={
                'class' : 'w-full py-2 px-6 rounded-lg border'
            }),
            'title': forms.TextInput(attrs={
                'class' : 'w-full py-2 px-6 rounded-lg border'
            })
        }

