from django.core.management.base import BaseCommand
from users.models import User
from django.contrib.auth.management.commands import createsuperuser
import requests
class Command(BaseCommand):

   def handle(self, *args, **options):
        # Check if a user record with the username 'awsadmin' exists in the database
        # If it does not exist, then create a super-user with that username,
        # Supply an email address and a password to it
        # So, now we have an admin user to manage our AWS RDS database
        """if not User.objects.filter(username="awsadmin").exists():
            User.objects.create_superuser("awsadmin", "lukeyoobee@gmail.com", "AWSAdmin123")"""
            
        url = 'http://kiwinco-userapi-dev.ap-southeast-2.elasticbeanstalk.com/api/create/'  # Replace with your API endpoint
        data = {
            'username': "awsadmin",
            'email': "lukeyoobee@gmail.com",
            'password': "AWSAdmin123",
            'is_staff': 'True',
            'is_superuser': 'True',
        }
        requests.post(url, data=data)
        