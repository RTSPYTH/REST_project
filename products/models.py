from django.contrib.auth import get_user_model
from django.db import models

from categories.models import Category

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ManyToManyField(Category, related_name='category')
    image = models.ImageField(upload_to='product_images')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_by', null=True)

    def __str__(self):
        return f"{self.name}"