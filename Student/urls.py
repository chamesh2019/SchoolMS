from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.StudentAddView.as_view()),
    path("", views.StudentListView.as_view()),
    path("<int:index_number>/", views.StudentDetailView.as_view()),
]