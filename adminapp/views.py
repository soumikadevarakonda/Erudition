from django.shortcuts import render

# Create your views here.
def adminhomepage(request):
    return render(request, 'adminapp/AdminHomePage.html')


def manage_users(request):
    return render(request, 'adminapp/manage_users.html')


def catalog_management(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'adminapp/catalog_management.html', {'books': books})

def view_reports(request):
    return render(request, 'adminapp/view_reports.html')


from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from projectapp.models import Book


# View for adding a new book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new book to the database
            return redirect('adminapp:catalog_management')  # Redirect back to catalog management page
    else:
        form = BookForm()  # Initialize an empty form for GET request

    return render(request, 'adminapp/add_book.html', {'form': form})


# View for editing an existing book
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()  # Save the updated book
            return redirect('adminapp:catalog_management')  # Redirect back to catalog management page
    else:
        form = BookForm(instance=book)  # Pre-populate the form with the existing book data

    return render(request, 'adminapp/edit_book.html', {'form': form, 'book': book})
