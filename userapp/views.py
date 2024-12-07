# userapp/views.py
from django.shortcuts import render
from projectapp.models import Book

def userhomepage(request):
    # Fetch all books from the catalog
    books = Book.objects.all()

    # Pass the books to the template
    return render(request, 'userapp/UserHomePage.html', {'books': books})
