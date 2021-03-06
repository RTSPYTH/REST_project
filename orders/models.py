from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id')
    count = models.IntegerField(null=False)
    total_price = models.IntegerField(null=True)
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordered_by', null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_id} -- {self.ordered_by}'
