from Ecommerce.apps.product.repositories import ProductRepository 

class ProductService:
    @staticmethod
    def search_products(filters):
        """Apply business rules to product search"""
        return ProductRepository.filter_products(**filters)
    