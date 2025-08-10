from django.db import models

class Author(models.Model): # Model for Author
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model): # Model for Book
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # ForeignKey to Author
    publication_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
