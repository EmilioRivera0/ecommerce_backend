from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    history = models.JSONField()

    def __str__(self):
        return self.user.username
