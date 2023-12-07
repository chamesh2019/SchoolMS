from django.db import models

# Create your models here.
class Grade(models.Model):
    grade = models.IntegerField()
    subgrade = models.CharField(max_length=2)
    subjects = models.ManyToManyField('Subject.Subject', related_name='grade_subjects', blank=False)

    def advance_grade(self, new_subjects):
        # Remove the existing subjects and increase grade by 1
        self.grade += 1
        self.subjects.clear()

        # Add the new subjects to the grade
        for subject_name in new_subjects:
            subject = Subject.objects.get(name=subject_name)
            self.subjects.add(subject)

        # Save the grade object
        self.save()
        