from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="startpoint")
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="endpoint")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flight_id = models.ManyToManyField(Flight,blank=True,related_name="passengers")
    
    def __str__(self):
        return f"{self.first} {self.last}"