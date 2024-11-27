from django.db import models
from slugify import slugify 
from django.utils.html import escape

class AppVisit(models.Model):
    app_name = models.CharField(max_length=255)
    date = models.DateField()
    visit_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('app_name', 'date')
