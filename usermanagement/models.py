from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    # Other fields

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # Specify custom related names for groups and user_permissions fields
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_users')
        