from django.urls import path
from .views import  ProductesListView,ProductesDetailView, productes, product_detail

urlpatterns = [
    path('', productes, name='productes'),
    path('product/<slug:product_slug>', product_detail, name='product'),
    path('api/productes/', ProductesListView.as_view(), name='api-productes'), 
    path('api/product/<int:product_id>/', ProductesDetailView.as_view(), name='product'), 
]
