from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

class ProductCategoryModel(models.Model):
    """
    Model representing product categories
    """

    category = models.CharField(max_length=50, unique=True)
    

    class Meta:
        verbose_name = _("ProductCategory")
        verbose_name_plural = _("ProductCategories")

    def __str__(self):
        return self.category

class ProductModel(models.Model):
    """
    Model repressing products
    """

    PUBLICATION_STATUS = {
        "DR": "Draft",
        "PB": "Public"
    }

    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(ProductCategoryModel, related_name="product_category", on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)
    publication_status = models.CharField(choices=PUBLICATION_STATUS, max_length=2, default="DR")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

