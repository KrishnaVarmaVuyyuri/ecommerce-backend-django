from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # ensures URL is returned

    class Meta:
        model = Product
        fields = "__all__"

