from django.urls import path
from .views import api_root, get_users

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/users/', get_users, name='get-users'),
]
