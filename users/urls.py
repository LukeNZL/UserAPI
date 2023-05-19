from django.urls import path
from .views import UserList, UserCreate, UserDelete, UserLogin


urlpatterns = [
    path('userlist/', UserList.as_view(), name='UserList'),
    path('create/', UserCreate.as_view(), name='UserCreate'),
    path('delete/', UserDelete.as_view(), name='UserDelete'),
    path('login/', UserLogin.as_view(), name='UserLogin'),

    # Add other URLs for different views
]
