from rest_framework import serializers
from .models import Recu

class RecuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recu
        fields = '__all__'