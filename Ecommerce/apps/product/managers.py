from django.db.models import Q
from django.db import models


class ProductCategoryManager(models.Manager):
    def get_all_categories(self):
        """Return all categories"""
        return self.all()


class ProductManager(models.Manager):
    def get_all_published_product(self):
        """Return all published product"""
        return self.filter(publication_status="PB")

    def filter_by_category(self, category):
        """Filter product by category"""
        return self.filter(category__pk=category)

    def filter_by_search(self, search):
        """Search in both name and description"""
        return self.filter(Q(name__icontains=search) | Q(description__icontains=search))

    def filter_by_price(self, min_price=None, max_price=None):
        """Filter product by price(min_price and max_price)"""
        if min_price:
            return self.filter(price__gte=min_price)
        if max_price:
            return self.filter(price__lte=max_price)
