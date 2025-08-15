# from django.urls import include, path
# from django.views import debug

# from .constants import API_V1_PATH

# # from .views import redirect_admin

# app_name = "core"

# urlpatterns = [
#     # Comment next line for real project and uncomment the second line
#     path("", debug.default_urlconf),
#     # path('', redirect_admin, name='redirect_admin'),
#     # path('app1/',
#     # include('Ecommerce.apps.app1.urls'),
#     # name='app1-urls'),
#     # path('app2/',
#     # include('Ecommerce.apps.app2.urls'),
#     # name='app2-urls'),
#     # REST API v1
#     path(
#         API_V1_PATH,
#         include("Ecommerce.apps.core.api.v1.urls"),
#         name="core_api_v1_urls",
#     ),
#     path(
#         API_V1_PATH,
#         include("Ecommerce.apps.product.api.v1.urls"),
#         name="product_api_v1_urls",
#     ),
# ]
