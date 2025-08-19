from django.urls import include, path

from Ecommerce.apps.order.api.v1 import urls as api_urls

urlpatterns = [path("order/api/v1/", include(api_urls, namespace="order"))]
