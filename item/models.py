from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    item_image = models.ImageField(null=True, blank=True, default='default.jpg')
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']