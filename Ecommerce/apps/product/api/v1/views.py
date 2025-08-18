from rest_framework.response import Response
from rest_framework.views import APIView

from Ecommerce.apps.product.api.v1 import serializers
from Ecommerce.apps.product.services import (ProductCategoryService,
                                             ProductService)


class ProductListView(APIView):
    def get(self, request):
        category = request.query_params.get("category")
        search = request.query_params.get("search")
        min_price = request.query_params.get("min_price")
        max_price = request.query_params.get("max_price")

        queryset = ProductService.get_all_published_products()
        queryset = ProductService.search_products(
            queryset,
            {
                "category": category,
                "search": search,
                "min_price": min_price,
                "max_price": max_price,
            },
        )
        serialized_data = serializers.ProductSerializer(queryset, many=True)

        return Response(data={"response": serialized_data.data})


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = ProductService.get_product(pk)
        serialized_data = serializers.ProductSerializer(instance=product)
        return Response(data={"response": serialized_data.data})