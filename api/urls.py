from django.urls import path, include

urlpatterns = [
    path('', include('api.routers'), name='api_router'),
]
