from django.urls import path
from core_app.views import CreateRestaurant, GetTodaysMenu, GetTodaysResults, UploadRestaurantMenu


urlpatterns = [
    path('menu', GetTodaysMenu.as_view(), name='menu'),
    path('results', GetTodaysResults.as_view(), name='results'),
    path('create-restaurant', CreateRestaurant.as_view(), name='create-restaurant'),
    path('update-menu', UploadRestaurantMenu.as_view(), name='update-menu')
]
