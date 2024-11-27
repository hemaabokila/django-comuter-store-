from django.contrib.sitemaps import Sitemap
from productes.models import Productes
from django.urls import reverse


class ProductesPageSitemap(Sitemap):
    def items(self):
        return Productes.objects.all()

    def location(self, obj):
        return reverse('productes')  
    

