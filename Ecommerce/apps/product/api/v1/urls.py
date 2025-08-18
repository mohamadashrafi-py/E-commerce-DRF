from django.urls import path

from .views import ProductListView, ProductDetailView, CategoryListView

app_name = "product"

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("categories/", CategoryListView.as_view(), name="category_list")
]
