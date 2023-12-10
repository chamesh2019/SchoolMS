from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

class CustomTokenRefreshView(TokenRefreshView):
    pass

class CustomTokenVerifyView(TokenVerifyView):
    pass