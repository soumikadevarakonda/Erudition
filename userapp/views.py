# userapp/views.py
from django.shortcuts import render
from projectapp.models import Book


def userhomepage(request):
    # Get the search query from the GET request, if present
    query = request.GET.get('q', '')  # Default to an empty string if no query

    # Filter books based on the query if it's present, otherwise fetch all books
    if query:
        books = Book.objects.filter(title__icontains=query)  # Case-insensitive search in the title
    else:
        books = Book.objects.all()  # Fetch all books if no search query is given

    # Pass the books to the template
    return render(request, 'userapp/UserHomePage.html', {'books': books})
