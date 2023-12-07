from django.db import models


class Term(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name


class Mark(models.Model):
    student = models.ForeignKey("Student.Student", on_delete=models.CASCADE)
    subject = models.ForeignKey("Subject.Subject", on_delete=models.CASCADE)
    marks = models.IntegerField()
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.student

    class Meta:
        unique_together = ('student', 'subject', 'term')