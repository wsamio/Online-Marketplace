from django.db.models import Q
from .models import Item

def searchItem(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    items = Item.objects.distinct().filter(Q(title__icontains=search_query))
        #items = Item.objects.distinct().filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    return items, search_query
