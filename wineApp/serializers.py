from .models import Wine
from rest_framework import serializers

#,country,description,designation,points,price,province,region_1,region_2,variety,winery

class WineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wine
        fields = ('country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery')