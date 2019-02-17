from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WineSerializer
from .models import Wine
from .utils import loadData
from django.http import HttpResponse

# Create your views here.
class Home(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer

def LoadData(request):
    loadData('/home/anmol/Downloads/winemag-data_first150k3ed116a.csv')
    return HttpResponse("hey!!")
