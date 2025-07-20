RETRIEVE:
Book.objects.get().values_list()  	#Retrieves all instances of Book created in a list format
output = <QuerySet [(1, '1984', 'George Orwell', 1949)]>