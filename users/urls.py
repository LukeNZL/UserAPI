from django.urls import path
from .views import UserList, UserCreate, UserDelete, UserLogin,UserEdit,LogoutView, UserView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', UserList.as_view(), name='UserList'),
    path('user/', UserView.as_view(), name='UserView'),

    path('userlist/', UserList.as_view(), name='UserList'),
    path('create/', UserCreate.as_view(), name='UserCreate'),
    path('delete/', UserDelete.as_view(), name='UserDelete'),
    path('login/', UserLogin.as_view(), name='UserLogin'),
    path('edit/', UserEdit.as_view(), name='UserEdit'),
    path('logout/', LogoutView.as_view(), name='logout'),
   
   
    # Add other URLs for different views
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
