from django.db import models
from django.forms import ModelForm

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name  = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    stock = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','stock','brand']
