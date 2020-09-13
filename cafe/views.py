from rest_framework import generics
from cafe.serializers import *
from cafe.filters import *
from django_filters.rest_framework import DjangoFilterBackend


class CoffeMachine(generics.ListAPIView):
    queryset = CoffeMachine.objects.all()
    serializer_class = CoffeMachineSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('model', 'product_type', 'water_line_compatible')


class CoffePod(generics.ListAPIView):
    queryset = CoffePods.objects.all()
    serializer_class = CoffePodsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('coffee_flavor','product_type','pack_size')




