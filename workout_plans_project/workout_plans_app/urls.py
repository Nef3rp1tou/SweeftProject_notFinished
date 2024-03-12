from django.urls import path
from .views import WorkoutPlanListCreate, WorkoutSessionListCreate

urlpatterns = [
    path('workout-plans/', WorkoutPlanListCreate.as_view(), name='workout-plan-list-create'),
    path('workout-sessions/', WorkoutSessionListCreate.as_view(), name='workout-session-list-create'),
]
