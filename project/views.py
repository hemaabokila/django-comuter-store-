from django.shortcuts import render
from productes.models import  Productes
from django.core.paginator import Paginator
from django.db.models import Q

def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def search_view(request):
    query = request.GET.get('q', '') 
    results = [] 

    if query:
        try:
            productes_results = Productes.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) | Q(title__icontains=query) 
            )
        except Exception :
            productes_results = []

        results = list(productes_results) 
    paginator = Paginator(results, 10) 
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    return render(request, 'search_results.html', {
        'query': query,
        'page_obj': page_obj,
    })
