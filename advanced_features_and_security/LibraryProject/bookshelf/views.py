from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# View list of books
@permission_required('books.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'templates/book_list.html', {'books': books})


# Create a new book
@permission_required('books.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'templates/form_example.html', {'form': form})


# Edit an existing book
@permission_required('books.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm(instance=book)
    return render(request, 'templates/form_example.html', {'form': form})


# Delete a book
@permission_required('books.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'templates/book_confirm_delete.html', {'book': book})