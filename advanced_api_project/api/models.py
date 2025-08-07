from django.db import models

#Model representing an Author
class Author(models.Model):
    name = models.CharField(max_length=100)  # sets Author's name (max 100 characters)

    def __str__(self):
        return self.name  #Helpful for displaying the author's name in admin & shell


# Model representing a Book
class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book (max 100 characters)
    publication_year = models.IntegerField()  # Year the book was published (as an integer)
    
    # Link each book to one author using a foreign key
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,      # Delete all books if the author is deleted
        related_name='books'           # Allows reverse lookup: author.books.all()
    )

    def __str__(self):
        return self.title  # Helps show readable book titles in admin & shell