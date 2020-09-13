from rest_framework import serializers
from cafe.models import *


class CoffeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeMachine
        fields = ('name',
                  'product_type',
                  'water_line_compatible',
                  'model')


class CoffePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffePods
        fields = ('name',
                  'product_type',
                  'coffee_flavor',
                  'pack_size')
