from django.urls import path, include
from rest_framework_simplejwt import views
from auth_app.views import CreateUser

urlpatterns = [
    path('login', views.TokenObtainPairView.as_view(), name="login"), # Request: username, password
    path('refresh', views.TokenRefreshView.as_view(), name="refresh"),  # Request: refresh
    path('verify', views.TokenVerifyView.as_view(), name="verify"),     # Request: token

    path('register', CreateUser.as_view(), name='register')
]
