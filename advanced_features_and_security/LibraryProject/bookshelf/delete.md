from bookshelf.models import Book


DELETE:
book = Book.objects.get(id=1)		#Retrieves the Book instance created to Delete
book.delete()				#Deletes the particular instance specified
(1, {'bookshelf.Book': 1})		#Displays the total number of object deleted, the model and the number of object deleted in from that model

Book.objects.all()
output = <QuerySet []>			#Returns an empty list when you try to retrieve all the books again

exit()      #to quit running on shell