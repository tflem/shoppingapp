from django.db import models

class Product(models.Model):
    """
    Model representing a product (e.g. Deodorant, Toothpaste).
    """
    item = models.CharField(max_length=50, help_text="Enter a product item (e.g. Deodorant, Toothpaste etc.)")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item
