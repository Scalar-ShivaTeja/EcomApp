from django.db import models
from django.utils.timezone import datetime
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price=models.DecimalField(decimal_places=2, max_digits=8)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name