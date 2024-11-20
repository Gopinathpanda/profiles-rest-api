from django.db import models

# Standard base classes you need to use when overwritting or customizing the default django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager  # Base user manager


class UserProfileManager():
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)  # for case sensitive email
        user = self.model(email=email, name=name)  # Create a new model object  that the UserProfileManager is representing
        user.set_password(password)  # comes from AbstractBaseUser class . Here password converts to a hash
        user.save(using=self._db)  # standard proceduce to save data
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True  # Automatically this field created by PermissionsMixin class
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()  # Class
    USERNAME_FIELD = 'email'  # Overwriting default USERNAME_FIELD with our email field for authentication
    REQUIRED_FIELDS = ['name']  # Additional required field along with email field

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email
