from Ecommerce.apps.product.models import ProductCategoryModel, ProductModel


class ProductCategoryRepository:
    @staticmethod
    def get_all_categories(self):
        return ProductCategoryModel.objects.get_all_categories()


class ProductRepository:
    @staticmethod
    def get_all_published_product(self):
        return ProductModel.objects.get_all_published_product()

    @staticmethod
    def filter(self, search=None, category=None, min_price=None, max_price=None):
        products = ProductModel.objects.get_all_published_product()

        if category:
            products.filter_by_category(category)

        if search:
            products.filter_by_search(search)

        if min_price or max_price:
            products.filter_by_price(min_price, max_price)
