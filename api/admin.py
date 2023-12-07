from django.contrib import admin

from api.models import Student, CustomUser

# Register your models here.
admin.site.register(Student)
admin.site.register(CustomUser)

