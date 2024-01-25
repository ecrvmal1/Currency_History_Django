from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Rate


class RateModelSerializer(ModelSerializer):
    rate = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Rate
        fields = '__all__'
