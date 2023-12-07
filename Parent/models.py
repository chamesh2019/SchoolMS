from django.db import models

# Create your models here.
class Parent(models.Model):
    user = models.OneToOneField("api.CustomUser", on_delete=models.CASCADE)
    student = models.ForeignKey("Student.Student", on_delete=models.CASCADE)
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
