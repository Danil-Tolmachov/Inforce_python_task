from django.urls import path
from rest_framework_simplejwt import views
from auth_app.views import CreateUser, VoteFor

urlpatterns = [
    path('register', CreateUser.as_view(), name='register'),
    path('login', views.TokenObtainPairView.as_view(), name="login"), # Request: username, password
    path('refresh', views.TokenRefreshView.as_view(), name="refresh"),  # Request: refresh
    path('verify', views.TokenVerifyView.as_view(), name="verify"),     # Request: token

    path('vote', VoteFor.as_view(), name='vote'),
]
