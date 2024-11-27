from django.shortcuts import render
from django.core.cache import cache
from productes.models import  Productes
from .models import AppVisit
from django.db.models import Sum, Q
from datetime import date
from django.shortcuts import render

def home_view(request):
    cached_data = cache.get('home_data')

    if not cached_data:
        visits = AppVisit.objects.filter(app_name="home").aggregate(
            today_visits=Sum('visit_count', filter=Q(date=date.today())),
            total_visits=Sum('visit_count')
        )
        
        collection = Productes.objects.order_by('-created_at')[:3]
        latest_productes = Productes.objects.order_by('-created_at')[:8]

        cached_data = {
            'today_visits': visits['today_visits'] or 0,
            'total_visits': visits['total_visits'] or 0,
            'latest_productes': latest_productes,
            'collection': collection,
        }

        cache.set('home_data', cached_data, 300) 

    return render(request, 'home.html', cached_data)
