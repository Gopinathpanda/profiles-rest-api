from django.db import models

# Standard base classes you need to use when overwritting or customizing the default django user model
from django.contrib.auth.models import AbstractBaseUser #This class provides basic user fields like password hashing and authentication methods.
from django.contrib.auth.models import PermissionsMixin #adds fields and methods to support user permissions and group membership, like is_superuser, is_staff, user_permissions, etc
from django.contrib.auth.models import BaseUserManager  # base manager class used to create user-related objects.
                                                        # You can inherit and override this class to define custom methods for user creation (like create_user and create_superuser).


class UserProfileManager(BaseUserManager): #In Django, managers like UserProfileManager are used to handle queries for a specific model (in this case, UserProfile),
                                            # but managers themselves don't have an objects attribute directly.
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)  #makes the email case-insensitive, ensuring that User@domain.com and user@domain.com are treated the same
        user = self.model(email=email, name=name)  # Create a new model object  that the UserProfileManager is representing
        user.set_password(password)  # comes from AbstractBaseUser class . Here password converts to a hash and stored
        user.save(using=self._db)  # standard procedure to save data
        return user

    def create_superuser(self, email, name, password):# Under the hood the python manage.py createsuperuser used this method
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

    objects = UserProfileManager()  # Class so that we can use it's functions like UserProfile.objects.create_user(email="user@example.com", name="John Doe", password="password123")
    USERNAME_FIELD = 'email'  # Overwriting default USERNAME_FIELD(by default) with our email field for authentication
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
