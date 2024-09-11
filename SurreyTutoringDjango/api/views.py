from django.shortcuts import render
from rest_framework import generics
from .models import price_list
from .serializers import price_list_serializer

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def prices(request):
    prices = price_list.objects.all()
    return render(request, 'pricing.html', {'prices': prices})

class price_list_view(generics.ListAPIView):
    queryset = price_list.objects.all()
    serializer_class = price_list_serializer
