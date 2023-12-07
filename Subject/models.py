from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255)
    bucket = models.BooleanField(default=False)
    required = models.BooleanField(default=True)
    stream = models.CharField(max_length=10, choices=[('6-9', 'Junior Secondary 6-9'), ('O/L', 'Ordinary Level (10-11)'), ('A/L', 'Advanced Level(12-13)')])
    
    def __str__(self) -> str:
        return self.name