from django.urls import path
from core_app.views import Test


urlpatterns = [
    path('test', Test.as_view())
]
