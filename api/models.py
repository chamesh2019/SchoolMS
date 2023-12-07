from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    index_number = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    name_with_initials = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=[('M', 'Male'), ('F', 'Female')])
    enrolled_date = models.CharField(max_length=20)
    address = models.TextField()
    special_notes = models.TextField(null=True, blank=True)
    
    
    def check_password(self, password):
        return self.password == password
    
    def __str__(self) -> str:
        return self.full_name
        

class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_index_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    nic = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    relation = models.CharField(max_length=25, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Guardian', 'Guardian')])
    special_notes = models.TextField()
    

    def __str__(self) -> str:
        return self.full_name


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)    
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
    