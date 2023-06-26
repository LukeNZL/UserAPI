from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    logged_in = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #change this back once superuser is made and remove unique from username
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []
   
    

