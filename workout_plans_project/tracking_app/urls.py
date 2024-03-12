from django.urls import path
from .views import WeightTrackingListCreate

urlpatterns = [
    path('weight-trackings/', WeightTrackingListCreate.as_view(), name='weight-tracking-list-create'),
]
