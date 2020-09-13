from django.db import models

# Create your models here.
class CoffeMachine(models.Model):
    name = models.TextField(max_length=70, blank=False, default='')
    product_type = models.CharField(max_length=70, blank=False, default='')
    water_line_compatible = models.BooleanField()
    model = models.CharField(max_length=200,blank=False, default='')

class CoffePods(models.Model):
    name = models.TextField(max_length=70, blank=False, default='')
    product_type = models.CharField(max_length=70, blank=False, default='')
    coffee_flavor = models.CharField(max_length=200,blank=False, default='')
    pack_size = models.CharField(max_length=200,blank=False, default='')



