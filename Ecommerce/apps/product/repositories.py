from Ecommerce.apps.product.models import ProductCategoryModel, ProductModel


class ProductCategoryRepository:
    @staticmethod
    def get_all_categories():
        return ProductCategoryModel.objects.get_all_categories()


class ProductRepository:
    @staticmethod
    def get_all_published_product():
        return ProductModel.objects.get_all_published_product()

    @staticmethod
    def filter_products(queryset, search=None, category=None, min_price=None, max_price=None):
        queryset = queryset

        if category:
            queryset.filter_by_category(category)

        if search:
            queryset.filter_by_search(search)

        if min_price or max_price:
            queryset.filter_by_price(min_price, max_price)

        return queryset