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
    
    @staticmethod
    def get_product(pk):
        """Return product object by pk"""
        return ProductRepository.get_product(pk)


class ProductCategoryService:
    @staticmethod
    def get_all_categories():
        """Return all product categories"""
        return ProductCategoryRepository.get_all_categories()
