from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WineSerializer
from .models import Wine
from .utils import loadData
from django.http import HttpResponse
from rest_framework import generics

#,country,description,designation,points,price,province,region_1,region_2,variety,winery

# Create your views here.
class Home(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer

class Filtered(generics.ListAPIView):
    serializer_class = WineSerializer
    
    
    def get_queryset(self):
        country = self.request.query_params.get('country', None)
        province = self.request.query_params.get('province', None)
        region_1 = self.request.query_params.get('region_1', None)
        region_2 = self.request.query_params.get('region_2', None)
        print(country)

        queryset = Wine.objects.all()
        if country is not None:
            queryset = queryset.filter(country = country)
        if province is not None:
            queryset = queryset.filter(province = province)
        if region_1 is not None:
            queryset = queryset.filter(region_1 = region_1)
        if region_2 is not None:
            queryset = queryset.filter(region_1 = region_2)

        return queryset


def LoadData(request):
    loadData('/home/anmol/Downloads/winemag-data_first150k3ed116a.csv')
    return HttpResponse("hey!!")
