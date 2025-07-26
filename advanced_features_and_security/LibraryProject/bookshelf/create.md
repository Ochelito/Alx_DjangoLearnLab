python manage.py shell


from bookshelf.models import Book  	#Imported Book model from Django-app to interact with it

CREATE:
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949) 	#creates new Book instance and saves it in 1 step
book 	#to check if our Book was updated successfully, based on expected output set in models.py
output = <Book: 1984 by George Orwell>