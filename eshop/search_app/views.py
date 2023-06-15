from django.shortcuts import render
from shop_app.models import Products
from django.db.models import Q

# Create your views here.


def search_result(request):
    query = None
    product = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        product = Products.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'query': query, 'products': product})
