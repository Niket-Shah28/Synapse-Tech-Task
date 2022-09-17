from django.db import models

# Create your models here.
class Event(models.Model):
    Event_Name= models.CharField(max_length=100)
    Start_Date=models.DateField()
    End_Date=models.DateField()
    No_of_People=models.IntegerField()
    Situation=models.BooleanField()
