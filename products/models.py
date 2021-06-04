from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products_img', blank=True)
    short_description = models.CharField(max_length=128, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} || {self.category}'