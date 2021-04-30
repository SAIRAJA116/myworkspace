from django.db import models

# Create your models here.
class A (models.Model):
    name=models.CharField(max_length=60)
    rollNo=models.CharField(max_length=10)
    percentage=models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.rollNo})"

