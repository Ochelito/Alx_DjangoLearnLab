from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields of the Book model in the serialization

    # Custom validation method for the 'publication_year' field
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            #Prevents future years from being used as the publication year
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value  #Returns the valid year when inputted

# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    #Nests related books inside the Author serializer, read-only
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']  #Serializes only the author's name and related books
