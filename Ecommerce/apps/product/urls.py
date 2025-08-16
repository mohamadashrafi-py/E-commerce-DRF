from django.urls import include, path

from Ecommerce.apps.product.api.v1 import urls as api_urls

urlpatterns = [path("product/api/v1/", include(api_urls, namespace="product"))]
