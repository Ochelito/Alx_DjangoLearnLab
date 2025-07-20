from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.SET_NULL, null=True, related_name='librarians')




""" Implementing Advanced Model Relationships in Django
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
Retrieve the librarian for a library."""
