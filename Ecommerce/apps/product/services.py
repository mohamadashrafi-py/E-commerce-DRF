from Ecommerce.apps.product.repositories import (ProductCategoryRepository,
                                                 ProductRepository)


class ProductService:
    @staticmethod
    def get_all_published_products():
        """Return all published products"""
        return ProductRepository.get_all_published_product()

    @staticmethod
    def search_products(queryset, filters):
        """Apply business rules to product search"""
        return ProductRepository.filter_products(queryset, **filters)


class ProductCategoryService:
    @staticmethod
    def get_all_products():
        """Return all product categories"""
        return ProductCategoryRepository.get_all_categories()
