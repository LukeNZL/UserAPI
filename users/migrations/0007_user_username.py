# Generated by Django 4.2.1 on 2023-06-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_superuser_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]
