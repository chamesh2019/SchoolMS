from django.contrib.auth.backends import ModelBackend

from api.models import Student

class MultipleModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            student = Student.objects.get(index_number=username)
            if student.user.check_password(password):
                return student.user
        except Student.DoesNotExist:
            pass
        
        
        return None