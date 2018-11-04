

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.
class UserProfileManager(BaseUserManager):
    """Help django to identify our custom user model"""

    def create_user(self, email, name, password=None):


        if not email:
            raise ValueError('User has to have email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

class userProfile(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get users full name."""

        return self.name 

    def get_short_name(self):

        return self.name

    def __str__(self):
        """Django need this to convert object into string"""

        return self.email 

