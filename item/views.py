from django.shortcuts import render, redirect
from .models import Category, Item
from .forms import CreateItemForm
from django.contrib.auth.decorators import login_required

def allItems(request):
    
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    context = {'items' : items, 'categories' : categories}
    
    return render(request, 'item/all-items.html', context)


def singleItem(request, pk):
    item = Item.objects.get(id=pk)
    related_items = Item.objects.filter(category = item.category, is_sold=False).exclude(id=pk)[0:3]
    context = {'item' : item, 'related_items' : related_items}


    return render(request, 'item/single-item.html', context)


@login_required(login_url='login')
def createItem(request):
    form = CreateItemForm()

    if request.method == 'POST':
        form = CreateItemForm(request.POST, request.FILES)
        item = form.save(commit=False)
        item.created_by = request.user
        item.save()

        return redirect('single-item', pk=item.id)

    context = {'form' : form}
    return render(request, 'item/create-item.html', context)

@login_required(login_url='login')
def deleteItem(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('all-items')


def editItem(request, pk):
    item = Item.objects.get(id=pk)
    form = CreateItemForm(instance=item)
    if request.method == 'POST':
        form = CreateItemForm(request.POST, request.FILES, instance=item)
        form.save()

        return redirect('single-item', pk=item.id)

    context = {'form' : form}
    return render(request, 'item/create-item.html', context)


def browseItem(request):
    items = Item.objects.filter(is_sold=False)
    
    context = {'items' : items}
    return render(request, 'item/browse.html', context)


