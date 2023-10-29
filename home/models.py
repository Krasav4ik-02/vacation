from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    position = models.CharField(max_length=100)

class WorkSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # Понедельник, Вторник, и т.д.
    start_time = models.TimeField()
    end_time = models.TimeField()

class WorkStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('на работе', 'На работе'), ('вне работы', 'Вне работы'), ('выходной', 'Выходной')])