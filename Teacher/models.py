from django.db import models

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField("api.CustomUser", on_delete=models.CASCADE)    
    full_name = models.CharField(max_length=255)
    name_with_initials = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    nic = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    position = models.CharField(max_length=256)
    post = models.TextField()
    qr_key = models.TextField()
    special_notes = models.TextField()
    teacher_grade = models.CharField(max_length=50)
    address = models.TextField()
    contact_number = models.CharField(max_length=12)
    enrolled_date = models.DateField(auto_now=False)
    teaching_started_date = models.DateField(auto_now=False)
    
    def __str__(self) -> str:
        return self.full_name
    
    
    
        
