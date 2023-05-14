from django.urls import path
from core_app.views import CreateRestaurant, GetTodaysMenu, GetTodaysResults, UploadRestaurantMenu


urlpatterns = [
    path('menu', GetTodaysMenu.as_view()),
    path('results', GetTodaysResults.as_view()),
    path('create-restaurant', CreateRestaurant.as_view()),
    path('update-menu', UploadRestaurantMenu.as_view())
]
