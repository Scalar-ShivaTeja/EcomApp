from django.db import models
from django.utils.timezone import datetime
# Create your models here.


class AuditData(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price=models.DecimalField(decimal_places=2, max_digits=8)
    is_available = models.BooleanField(default=False)
    category=models.ForeignKey('Category', on_delete=models.SET_NULL,
                               null=True,related_name='products')

    def __str__(self):
        return self.name


class Category(AuditData):
    name=models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name