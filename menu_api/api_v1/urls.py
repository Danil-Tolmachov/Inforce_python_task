from django.urls import include, path


urlpatterns = [
    path('', include('auth_app.urls')),
    path('', include('core_app.urls')),
]
