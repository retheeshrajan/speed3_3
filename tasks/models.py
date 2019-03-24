from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    image=models.ImageField(null=True, blank=True)
    owner=models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name