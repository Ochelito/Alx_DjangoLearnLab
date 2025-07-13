UPDATE:
book = Book.objects.get(id=1)		#Retrieves the first instance created to modify
book.title="Nineteen Eighty-Four"	#updated the title of that instance
book					#to check if updated successfully
output = <Book: Nineteen Eighty-Four by George Orwell>
