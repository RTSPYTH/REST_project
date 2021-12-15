from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категории')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='parent_category')

    def __str__(self):
        if self.parent:
            return f'{self.name}-->{self.parent}'
        return f'{self.name}'