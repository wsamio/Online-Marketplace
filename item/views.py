from django.shortcuts import render
from .models import Category, Item

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
