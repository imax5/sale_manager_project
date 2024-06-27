from django.db import models

class Unit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    unit = models.ForeignKey('Unit', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductWarehouse(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    buy_price = models.DecimalField('Buy price', max_digits=10, decimal_places=2)
    buy_price_usd = models.DecimalField('Buy price $', max_digits=10, decimal_places=2)
    sell_price = models.DecimalField('Sell price', max_digits=10, decimal_places=2)
    updated = models.DateTimeField('Updated', auto_now=True)
    created = models.DateTimeField('Created', auto_now_add=True)

    def __str__(self):
        return self.product.name