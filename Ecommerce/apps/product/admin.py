from django.contrib import admin
from Ecommerce.apps.product.models import ProductModel, ProductCategoryModel

@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
    search_fields = ("category",)
    list_per_page = 6

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    search_fields = ("name",)
    list_filter = ("category", "created_at")
    list_per_page = 6