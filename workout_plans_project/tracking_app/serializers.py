from rest_framework import serializers
from .models import WeightTracking

class WeightTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightTracking
        fields = '__all__'
