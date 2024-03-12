from django.db import models
from users_app.models import User

class WeightTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()

    def __str__(self):
        return f'{self.user.username} - {self.date}'
