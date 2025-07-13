python manage.py shell


from bookshelf.models import Book  	#Imported Book model from Django-app to interact with it

CREATE:
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949) 	#creates new Book instance and saves it in 1 step
book 	#to check if our Book was updated successfully, based on expected output set in models.py
output = <Book: 1984 by George Orwell>

RETRIEVE:
Book.objects.all().values_list()  	#Retrieves all instances of Book created in a list format
output = <QuerySet [(1, '1984', 'George Orwell', 1949)]>

UPDATE:
book = Book.objects.get(id=1)		#Retrieves the first instance created to modify
book.title="Nineteen Eighty-Four"	#updated the title of that instance
book					#to check if updated successfully
output = <Book: Nineteen Eighty-Four by George Orwell>

DELETE:
book = Book.objects.get(id=1)		#Retrieves the Book instance created to Delete
book.delete()				#Deletes the particular instance specified
(1, {'bookshelf.Book': 1})		#Displays the total number of object deleted, the model and the number of object deleted in from that model

Book.objects.all()
output = <QuerySet []>			#Returns an empty list when you try to retrieve all the books again

