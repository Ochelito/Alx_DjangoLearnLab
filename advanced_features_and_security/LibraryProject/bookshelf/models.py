from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_date})"
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth=None):
        if not email:
            raise ValueError("Email is required")
        if not date_of_birth:
            raise ValueError("Date of birth is required")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, date_of_birth=None):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must gave is_staff=True.')
        
        if not extra_fields.get('is_superuser'):
            raise ValueError('Supperuser must have is_superuser=True')

        return self.creat_user(username, email, password, date_of_birth)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    objects = CustomUserManager()