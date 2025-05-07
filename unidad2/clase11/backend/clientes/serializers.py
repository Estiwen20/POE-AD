from rest_framework import serializers
from .models import Loro

class LoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loro
        fields = '__all__'
