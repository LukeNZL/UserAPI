from django.core.management.base import BaseCommand
from users.models import User
from django.contrib.auth.management.commands import createsuperuser

class Command(createsuperuser.Command):

   def handle(self, *args, **options):
        # Check if a user record with the username 'awsadmin' exists in the database
        # If it does not exist, then create a super-user with that username,
        # Supply an email address and a password to it
        # So, now we have an admin user to manage our AWS RDS database
        if not User.objects.filter(username="awsadmin").exists():
            username="awsadmin"
            email="lukeyoobee@gmail.com"
            password="AWSAdmin123"
            
            User.objects.create(username, email, password)
            
