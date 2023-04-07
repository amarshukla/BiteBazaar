from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('Email can not be null.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    username = None
    email = models.EmailField(verbose_name='email address', unique=True)
    address = models.CharField(max_length=250)
    dob = models.DateField()
    mobile = models.CharField(max_length=30)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """ Return string representation of our user """
        return self.email