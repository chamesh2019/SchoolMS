from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField("api.CustomUser", on_delete=models.CASCADE)
    index_number = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    name_with_initials = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=[('M', 'Male'), ('F', 'Female')])
    enrolled_date = models.CharField(max_length=20)
    address = models.TextField()
    special_notes = models.TextField(null=True, blank=True)
    
    selected_subjects = models.ManyToManyField('Subject.Subject', related_name='selected_subjects', blank=True)
    
    def __str__(self) -> str:
        return self.full_name
        
