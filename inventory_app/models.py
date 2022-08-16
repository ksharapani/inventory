from django.db import models


class Supplier(models.Model):
    objects = None

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    objects = None

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey(Supplier, related_name='inventory_supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

