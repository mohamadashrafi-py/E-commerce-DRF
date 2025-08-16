from rest_framework import serializers
from Ecommerce.apps.product.models import ProductModel, ProductCategoryModel

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = ("category",)

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    
    class Meta:
        model = ProductModel
        fields = (
            'name', 'description', 'price', 
            'publication_status', 'created_at', 'updated_at',
            'category'
        )