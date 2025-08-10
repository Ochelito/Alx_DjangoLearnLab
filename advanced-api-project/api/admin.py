from django.contrib import admin
from .models import Author, Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
# This code registers the Author and Book models with the Django admin site,
# allowing them to be managed through the admin interface.