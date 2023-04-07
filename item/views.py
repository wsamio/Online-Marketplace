from django.shortcuts import render
from .models import Category, Item

def allItems(request):
    
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    context = {'items' : items, 'categories' : categories}
    
    return render(request, 'item/all-items.html', context)


def singleItem(request, pk):
    item = Item.objects.get(id=pk)
    context = {'item' : item }

    return render(request, 'item/single-item.html', context)
