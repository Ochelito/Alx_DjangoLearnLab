from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    choices = [
        ('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=choices)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

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



""" 
def __str__(self):
        if self.library:
            return f"{self.name} is the librarian for {self.library}" If self.library is None (because SET_NULL is allowed), this will print:
John is the librarian for None — not ideal.

Implementing Advanced Model Relationships in Django
mandatory
Objective: Master Django’s ORM capabilities by creating a set of models that demonstrate the use of ForeignKey, ManyToMany, and OneToOne relationships. This task will help you understand how to model complex data relationships in a Django project effectively.

Task Description:
Duplicate the previous project directory Introduction_ to_ Django, rename it to django-models and add a new app named relationship_app where you’ll define models that showcase complex relationships between entities using ForeignKey, ManyToMany, and OneToOne fields.

Steps:
Create the relationship_app App:

Within your Django project directory, generate a new app: python manage.py startapp relationship_app.
Define Complex Models in relationship_app/models.py:

Author Model:
name: CharField.
Book Model:
title: CharField.
author: ForeignKey to Author.
Library Model:
name: CharField.
books: ManyToManyField to Book.
Librarian Model:
name: CharField.
library: OneToOneField to Library.
Apply Database Migrations:

Run migrations to create your model tables: python manage.py makemigrations relationship_app followed by python manage.py migrate.
Implement Sample Queries:

Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of the following of relationship:
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.




3. Implement Role-Based Access Control in Django
mandatory
Objective: Implement role-based access control within a Django application to manage different user roles and permissions effectively. You will extend the User model and create views that restrict access based on user roles.

Task Description:
In your Django project, you will extend the Django User model to include user roles and develop views that restrict access based on these roles. Your task is to set up this system by creating a new model for user profiles, defining views with access restrictions, and configuring URL patterns.

Step 1: Extend the User Model with a UserProfile
Create a UserProfile model that includes a role field with predefined roles. This model should be linked to Django’s built-in User model with a one-to-one relationship.

Fields Required:
user: OneToOneField linked to Django’s User.
role: CharField with choices for ‘Admin’, ‘Librarian’, and ‘Member’.
Automatic Creation: Use Django signals to automatically create a UserProfile when a new user is registered.
Step 2: Set Up Role-Based Views
Create three separate views to manage content access based on user roles:

Views to Implement:

An ‘Admin’ view that only users with the ‘Admin’ role can access, the name of the file should be admin_view
A ‘Librarian’ view accessible only to users identified as ‘Librarians’. The file should be named librarian_view
A ‘Member’ view for users with the ‘Member’ role, the name of the file should be member_view
Access Control:

Utilize the @user_passes_test decorator to check the user’s role before granting access to each view.
Step 3: Configure URL Patterns
Define URL patterns that will route to the newly created role-specific views. Ensure that each URL is correctly linked to its respective view and that the URLs are named for easy reference.

URLs to Define:
A URL for the ‘Admin’ view.
A URL for the ‘Librarian’ view.
A URL for the ‘Member’ view.
Step 4: Create Role-Based HTML Templates
For each role, create an HTML template to display relevant content when users access their respective views.

Templates to Create:

admin_view.html for Admin users.
librarian_view.html for Librarians.
member_view.html for Members.



0. Implementing a Custom User Model in Django
mandatory
Objective: Customize Django’s user model to suit the specific needs of your application, demonstrating an understanding of extending Django’s authentication system.

Task Description:
For this task, you will replace Django’s default user model with a custom user model that includes additional fields and functionality. This is a critical feature for applications that require user attributes beyond Django’s built-in user model.

Step 1: Set Up the Custom User Model
Duplicate the previous Django project directory django-models and rename it to advanced_features_and_security
Create a custom user model by extending AbstractUser, adding custom fields that are relevant to your application’s needs.

Fields to Add:

date_of_birth: A date field.
profile_photo: An image field.
Step 2: Update Settings to Use the Custom User Model
Configure Django to use this custom user model for all user-related functionalities.

Settings Configuration:
In your project’s settings.py, set the AUTH_USER_MODEL to point to your new custom user model.
Step 3: Create User Manager for Custom User Model
Implement a custom user manager that handles user creation and queries, ensuring it can manage the added fields effectively.

Custom Manager Functions to Implement:
create_user: Ensure it handles the new fields correctly.
create_superuser: Ensure administrative users can still be created with the required fields.
Step 4: Integrate the Custom User Model into Admin
Modify the Django admin to support the custom user model, ensuring that administrators can manage users effectively through the Django admin interface.

Admin Modifications Required:
Define a custom ModelAdmin class that includes configurations for the additional fields in your user model.
Step 5: Update Your Application to Use the Custom User Model
Adjust any part of your application that references the user model to use the new custom model.

Application Updates:
Update all foreign keys or user model references in your other models to use the custom user model.
Deliverables:
models.py: Include your custom user model and custom user manager.
admin.py: Set up the admin interface to manage the custom user model effectively.
settings.py: Modify to specify the custom user model as the default for the project.
"""
