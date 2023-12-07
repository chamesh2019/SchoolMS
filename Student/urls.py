from django.urls import path
from . import views

urlpatterns = [
    path("students/add", views.StudentAddView.as_view()),
    path("students", views.StudentListView.as_view()),
    path("students/<int:index_number>", views.StudentDetailView.as_view()),
]