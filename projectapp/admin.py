from django.contrib import admin

# Register your models here.
# projectapp/admin.py


from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_available')  # Display columns in the admin
    search_fields = ('title', 'author')  # Search functionality in the admin
