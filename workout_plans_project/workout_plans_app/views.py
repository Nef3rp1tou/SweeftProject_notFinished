from rest_framework import generics
from .models import WorkoutPlan, WorkoutSession
from .serializers import WorkoutPlanSerializer, WorkoutSessionSerializer

class WorkoutPlanListCreate(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

class WorkoutSessionListCreate(generics.ListCreateAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
