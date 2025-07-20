from django.db import models
from django.contrib.auth import User
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

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.SET_NULL, null=True, related_name='librarians')

    def __str__(self):
        if self.library:
            return f"{self.name} is the librarian for {self.library}"
        else:
            return f"{self.name} is not assigned to any library"

class UserProfile(models.Model):

    ROLE_CHOICES = [
        ('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
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
"""
