from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/', blank=True, null=True)
    image = models.ImageField(upload_to='books/images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
