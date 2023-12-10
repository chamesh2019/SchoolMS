from django.urls import path
from . import views

urlpatterns = [
    path("token/", views.CustomTokenObtainPairView.as_view(), name="Token_view"),
    path("token/refresh", views.CustomTokenRefreshView.as_view(), name="Token_refresh"),
    path("token/verify", views.CustomTokenVerifyView.as_view(), name="Token_verify"),
]
