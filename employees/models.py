from django.contrib.auth.models import User
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    is_fired = models.BooleanField(default=False)
    date_of_termination = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name
