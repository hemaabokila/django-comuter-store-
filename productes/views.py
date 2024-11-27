from django.shortcuts import render ,get_object_or_404
from django.db.models import Count
from .models import Productes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductesSerializer

class ProductesListView(APIView):
    def get(self, request):
        productes = Productes.objects.all().order_by('-created_at')
        serializer = ProductesSerializer(productes, many=True)
        return Response(serializer.data)

class ProductesDetailView(APIView):
    def get(self, request, product_id):
        try:
            product = Productes.objects.get(id=product_id)
            serializer = ProductesSerializer(product)
            return Response(serializer.data)
        except Productes.DoesNotExist:
            return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)

def productes(request):

    selected_categories = request.GET.getlist('category') 
    selected_brands = request.GET.getlist('brand')  
    productes = Productes.objects.all()
    if selected_categories:
        productes = productes.filter(category__name__in=selected_categories)
    if selected_brands:
        productes = productes.filter(brand__name__in=selected_brands)
    categories = Productes.objects.values('category__name').annotate(count=Count('id'))
    brands = Productes.objects.values('brand__name').annotate(count=Count('id'))

    context = {
        'productes': productes,
        'categories': categories,
        'brands': brands,
        'selected_categories': selected_categories,
        'selected_brands': selected_brands,
    }
    return render(request, 'productes.html', context)

def product_detail(request, product_slug):
    product = get_object_or_404(Productes, slug=product_slug)
    return render(request, 'product_detail.html', {'product': product})
