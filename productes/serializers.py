from rest_framework import serializers
from .models import  Productes


class ProductesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productes
        fields = '__all__'