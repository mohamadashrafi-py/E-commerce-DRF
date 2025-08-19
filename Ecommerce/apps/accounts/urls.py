from django.urls import include, path

from Ecommerce.apps.accounts.api.v1 import urls as api_urls

urlpatterns = [path("accounts/api/v1/", include(api_urls, namespace="accounts"))]
