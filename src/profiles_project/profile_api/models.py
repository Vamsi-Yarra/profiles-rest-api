from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """
    Helps django work with our custom user model
    """
    def create_user(self,email,name,password=None):
        """
        Creates a User Profile Object
        """
        if not email:
            raise ValueError('User must have an email address')

        #Mormailize the email (keeping email in smaller case)
        email = self.normalize_email(email)
        user = self.model(email = email, name= name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """
        Creates and saves new super user with given details
        """
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """
    Represent a UserProfile inside our system
    """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Used to get the User's Full name
        """
        return self.name

    def get_short_name(self):
        """
        Used to get the User's short name
        """
        return self.name

    def __str__(self):
        """
        Returns a string when Object is printed
        """
        return self.email

class ProfileFeedItem(models.Model):
    """Profile Status Update"""
    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
# CASCADE means it deletes the status on deleting the profiles
    status_text= models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return Model as a string"""
        return self.status_text
