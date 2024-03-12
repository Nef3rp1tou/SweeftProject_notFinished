from rest_framework import generics
from .models import WeightTracking
from .serializers import WeightTrackingSerializer

class WeightTrackingListCreate(generics.ListCreateAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer
