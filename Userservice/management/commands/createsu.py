import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not User.objects.filter(username="username").exists():
           # password = os.environ.get("SUPERUSER_PASSWORD")
            password = "admin123"
            
            if password is None:
                raise ValueError("Password not found")
            User.objects.create_superuser(
                username="admin",
                email="lukeyoobee@gmail.com", 
                password=password,
            )
            print("Superuser has been created.")
        else:
            print("Superuser exists")