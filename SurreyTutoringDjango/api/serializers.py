from rest_framework import serializers
from .models import price_list

class price_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = price_list
        fields = '__all__'

