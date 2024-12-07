from django import forms
from projectapp.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'pdf', 'is_available']  # Specify the fields to be included
