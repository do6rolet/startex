from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'articule', 'name', 'price_in', 'price_out']
