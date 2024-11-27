from django.db import models
from slugify import slugify
import random

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Productes(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    prise=models.FloatField(max_length=100)
    prise2 = models.FloatField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='Productes/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            while Productes.objects.filter(slug=slug).exists():
                slug = f"{slug}-{random.randint(1, 1000)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/productes/product/{self.slug}"


